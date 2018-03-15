import zmq

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REP)
sock.bind("tcp://127.0.0.1:5678")

sockPub = context.socket(zmq.PUB)
sock.bind("tcp://127.0.0.1:5680")

# Run server
while True:
    getM = sock.recv()
    getM = getM.decode()
    print("[Server] received: " + getM)
    sendM = getM
    sock.send_string(sendM)
    sockPub.send_string(sendM)
    print("[Server] sent: " + sendM)