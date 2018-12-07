#！ /usr/bin/env python
# -*- coding:utf-8 -*-
import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=('192.168.0.21',2232)
s.bind(host)
s.listen(3)
while True:
    a,b=s.accept()
    msg=a.recv(1024)
    print(msg.decode('utf-8'))
    reg='asd'
    a.send(reg.encode('utf-8'))