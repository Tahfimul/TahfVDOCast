import socket
import cv2
import struct
import pickle
import time

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
s.listen(5)



conn, address = s.accept()

data = b""

payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))

while True:

    # msg = conn.recv(4096)
    # print(len(data) < payload_size)
    # print(msg)
    # Receive header content
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(1)
    print("Done Recv: {}".format(len(data)))
    #Length of header
    packed_msg_size = data[:payload_size]
    print(packed_msg_size)
    # Header content
    data = data[payload_size:]
    print(data)
    # Size of message extracted from header value [HEADER]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print(msg_size)
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    print(frame_data)
    print("\n\n")
    data = data[msg_size:]
    print(data)
    frame=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    frame = cv2.imdecode(frame, cv2.IMREAD_COLOR)
    cv2.imshow('ImageWindow',frame)
    cv2.waitKey(1)

        # print(msg)
        # data = cv2.imencode('.jpg', msg)[1]
        # print(data)
