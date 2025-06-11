import zmq

context = zmq.Context()
socket = context.socket(zmq.SUB)
socket.connect("tcp://localhost:5555")  # Subscriber connects to the publisher's port

# Subscribe to all messages
socket.setsockopt_string(zmq.SUBSCRIBE, "gyro")  # Subscribe to all topics

print("Waiting for messages...")

while True:
    message = socket.recv_string()  # Receive messages
    print(f"Received: {message}")