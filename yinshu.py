# for i in range(1, 101):
# #     b = 0
# #     for j in range(1, i):
# #         if i % j == 0:
# #             b = b + j
# #     if i == b:
# #         print(i)
import socket
a=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
a.connect(('192.168.0.21',12234))
aaa='das'
a.send(aaa.encode('uft-8'))
msg=a.recv(1024)
print(msg.decode('utf-8'))