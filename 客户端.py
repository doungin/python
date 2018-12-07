import socket

# 创建socket   封装协议

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

# 连接服务器
soc.connect(('192.168.0.33',11011))
# 发送请求
aaa = '赵某人'
soc.send(aaa.encode('utf-8'))
# 接收请求
msg = soc.recv(1024)
print(msg.decode('utf-8'))





#
#
# # UTP



# # 创建socket   封装协议
# soc = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# # 连接服务器
# soc.connect(('192.168.0.44',3000))
# # 发送请求
# while True:
#     aaa = input('刘大爷：')
#     soc.send(aaa.encode('utf-8'))
#     msg = soc.recv(1024)# 接收请求
#     print('魔镜:',msg.decode('utf-8'))
