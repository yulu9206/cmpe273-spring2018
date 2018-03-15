import zmq
import sys
import threading

# ZeroMQ Context
context = zmq.Context()

# Define the socket using the "Context"
sock = context.socket(zmq.REQ)
sock.connect("tcp://127.0.0.1:5678")

sockPub = context.socket(zmq.SUB)

# Define subscription and messages with prefix to accept.
sockPub.setsockopt_string(zmq.SUBSCRIBE, "[")
sockPub.connect("tcp://127.0.0.1:5680")

# Send a "message" using the socket
user = sys.argv[1]
connectS = "User[ {} ] Connected to the chat server.".format(user)
sock.send_string(connectS)
# print("client sent: " + connectS)
connectR = sock.recv()
connectR = connectR.decode()
print (connectR)

def send():
    while True:
        sendM = input("[ {} ] >".format(user))
        sendM = "[{}]: ".format(user) + sendM
        sock.send_string(sendM)
        print("client sent: " + sendM)
        getM = sock.recv()
        getM = getM.decode()
        print ("client received: " + getM)


def get():
    while True:    
        getM = sockPub.recv()
        getM = getM.decode()
        print("getM")
        if getM[0] == 'U':
            print('\n', getM)
        else:
            getMC = getM
            getMC.split('>', 1)
            getMC.strip('[ ')
            getMC.strip(' ]')
            if getMC != user:
                print ('\n', getM)

threading.Thread(target=get).start()
threading.Thread(target=send).start()
