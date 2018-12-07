# goods=[
#     {'name':'电脑','price':1999},
#     {'name':'鼠标','price':10},
#     {'name':'游艇','price':20},
#     {'name':'美女','price':998},
# ]
# a=int(input('总资产'))
# for i,j in enumerate(goods):
#     print(i+1,j)
# c=[]
# while True:
#     b=int(input("商品号"))
#     for f,g in enumerate(goods):
#         if b == f+1:
#             c.append(g)
#     print(c)
#     if  b == 0 :
#         break
#         print(c)#（已经购买的所有商品）
# z=len(c)
# k=0
# t=[]
# for l in range(z):
#     s=c[l]['price']
#     t.append(s)
# # print(s)
# for h in t:
#     k+=h
# print(k)#k=购买商品总额
# if k <= a:
#     print('购买成功')
# if k > a:
#     print('购买失败')
# while True:
#     u=int(input('余额不足，是否充值'))
#     a=a+u
#     j=a-k
#     if  a >= k:
#         print("购买成功",'余额',j)
#         break
#     elif  a< k:
#         continue
#     if u == 0:
#         d=int(input('钱不够，是否移除商品'))
#     if d == 0:
#         print('告辞')
#         break
#     for o, p in enumerate(c):
#         if d == o+1:
#             c.remove(p)
#             # print(c)
#     x=len(c)
#     u=[]
#     for g in range(x):
#         s = c[g]['price']
#         u.append(s)
#     print(u)
#     m=0
#     for h in u:
#         m += h
#     # print(m)
#     if a > m:
#         n=a-m
#         print('购买成功','余额',n)
#         break







import socket
s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
host=('192.168.0.33',11011)
s.bind(host)
s.listen()
while True:
    a,b=s.accept()
    msg=a.recv(1024)
    print(msg.decode('utf-8'))
    reg='who are you'
    a.send(reg.encode('utf-8'))