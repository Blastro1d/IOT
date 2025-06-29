"""
lab2_sensor_template
----------------

sensor reading example T.R. Walstra, may 2024
"""

import argparse
import asyncio
import logging
import struct
from bleak import BleakClient, BleakScanner
import zmq

BLE_UUID_ACCEL_SENSOR_DATA = "4664E7A1-5A13-BFFF-4636-7D0A4B16496C"
exit_flag = False

logger = logging.getLogger(__name__)
context = zmq.Context()
socket = context.socket(zmq.PUB)
socket.bind("tcp://*:6000")

def publish_data(data):
    socket.send_string(f"{"nothing"} {"nothing"}")
    socket.send_string(f"{"Accel all:"} {str(data[0]), str(data[1]), str(data[2])}")
    socket.send_string(f"{"Accel x:"} {str(data[0])}")
    socket.send_string(f"{"Accel y:"} {str(data[1])}")
    socket.send_string(f"{"Accel z:"} {str(data[2])}")
    socket.send_string(f"{"Gyro all:"} {str(data[3]), str(data[4]), str(data[5])}")
    socket.send_string(f"{"Gyro x:"} {str(data[3])}")
    socket.send_string(f"{"Gyro y:"} {str(data[4])}")
    socket.send_string(f"{"Gyro z:"} {str(data[5])}")

def notification_handler(sender,data):
    decoded_values = struct.unpack('ffffff', bytes(data))
    publish_data(decoded_values)
    print(decoded_values)

async def main(args: argparse.Namespace):
    global exit_flag

    logger.info("starting scan...")

    device = await BleakScanner.find_device_by_name(
          args.name, cb=dict(use_bdaddr=args.macos_use_bdaddr))
    if device is None:
        logger.error("could not find device with name '%s'", args.name)
        return

    print("connecting to device...")
    print("device name:", device.name)
    print("device addr:", device.address)
    print("services: ", args.services)

    async with BleakClient(device, services=args.services) as client:
        logger.info("connected")

        while not exit_flag:
            await asyncio.sleep(0.05)
            sensor_data = await client.read_gatt_char(BLE_UUID_ACCEL_SENSOR_DATA)
            notification_handler(client, sensor_data)
            print(".")

        logger.info("disconnecting...")

    logger.info("disconnected")


if __name__ == "__main__":

#execute this file as: "python lab2_sensor.py --name <arduino_local_name>


    parser = argparse.ArgumentParser()

    device_group = parser.add_mutually_exclusive_group(required=True)

    device_group.add_argument(
        "--name",
        metavar="<name>",
        help="the name of the bluetooth device to connect to",
    )
    device_group.add_argument(
        "--address",
        metavar="<address>",
        help="the address of the bluetooth device to connect to",
    )

    parser.add_argument(
        "--macos-use-bdaddr",
        action="store_true",
        help="when true use Bluetooth address instead of UUID on macOS",
    )

    parser.add_argument(
        "--services",
        nargs="+",
        metavar="<uuid>",
        help="if provided, only enumerate matching service(s)",
    )

    parser.add_argument(
        "-d",
        "--debug",
        action="store_true",
        help="sets the log level to debug",
    )

    args = parser.parse_args()

    log_level = logging.DEBUG if args.debug else logging.INFO
    logging.basicConfig(
        level=log_level,
        format="%(asctime)-15s %(name)-8s %(levelname)s: %(message)s",
    )

    asyncio.run(main(args))

