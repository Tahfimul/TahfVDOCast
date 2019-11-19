import socket
import cv2
import base64
import struct
import pickle


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname()', PORT))

vc = cv2.VideoCapture('main_anim.gif')
c=1

while True:
    #Read video frames using OpenCV and send hex values over Socket
    if vc.isOpened():
        rval , frame = vc.read()
    else:
        rval = False

    while rval:
        rval, frame = vc.read()
        if rval == False:
            break

        result, frame = cv2.imencode('.jpg', frame)
        data = pickle.dumps(frame, 0)
        size = len(data)
        # clientsocket.send(frame)
        print(data)
        # [HEADER DENOTATED BY HEX REPRESENTAION OF SIZE OF DATA] [FOLLOWED BY THE DATA]
        s.sendall(struct.pack(">L", size) + data)


        # print(data.tostring())

        c = c + 1
    print("Packets Sent. Closing...")
    s.close()
    vc.release()


# if vc.isOpened():
#     rval , frame = vc.read()
# else:
#     rval = False
#
# while rval:
#     rval, frame = vc.read()
#     if rval == False:
#         break
#
#
#     print(frame)
#
#     data = cv2.imencode('.jpg', frame)[1]
#     jpg_as_text = base64.b64encode(data)
#     # print(jpg_as_text)
#     jpg_original = base64.b64decode(jpg_as_text)
#     break
#     # print(jpg_original)
#     # for i in data:
#     #     print(i)
#     # clientsocket.send(data)
#     c = c + 1
#     cv2.waitKey(1)
