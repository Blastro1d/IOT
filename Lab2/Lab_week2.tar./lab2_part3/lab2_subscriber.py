import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")

socket.setsockopt_string(zmq.SUBSCRIBE, "Accel")

print("Waiting for messages...")

while True:
    message = socket.recv_string()
    print(f"Received: {message}")