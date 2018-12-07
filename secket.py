# # secket：套接字，接受了网络间通讯的基本功能（向网络发送请求，应答网络请求）
# # server 端
import socket
# TCP
# 创建一个socket ,封装协议（第一个是ipv4协议，第二个是tcp协议）
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 绑定ip和端口号 bind接受的参数是元组
host = ('192.168.0.33',4452)    #127.0.0.1环回地址
s.bind(host)
# 监听 数字指的是：最大等待数
s.listen(3)
while True:
    #接受请求
    a,b = s.accept()      # 第一个结果a：是客户端的链接信息  # 第二个结果b：是客户端的IP地址和端口号
    #接收数据
    msg = a.recv(1024)      #1024代表的是 ：每次接收的最大字节数
    print(msg.decode('utf-8'))
    #发送响应
    reg = '你是谁'
    a.send(reg.encode('utf-8'))










#
# # UDP
# # 创建一个socket ,封装协议（第一个是ipv4协议，第二个是tcp协议）
# s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)       #UDP跟TCP协议不一样
# # 绑定ip和端口号 bind接受的参数是元组
# host = ('192.168.0.44',3000)    #127.0.0.1环回地址
# s.bind(host)
# while True:
#     a,b=s.recvfrom(1024)   # 第一个变量a，客户端发送的请求数据。   第二个变量b,客户端的IP喝端口号
#     print(a.decode('utf-8'))
#     # print(b)
#     msg=input('NPC：')
#     s.sendto(msg.encode('utf-8'),b)
