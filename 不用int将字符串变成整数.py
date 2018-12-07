a =input('数字')
b = a[::-1]
s = 0
for i,j in enumerate(b):
    # print(i,j)
    for q in range(10):          ## 不用int将字符串变整数
        if str(q) == j:
            q=q*10**i
            s=s+q
print(s)
print(type(s))


#
#
#
#
#
#









# a=input('请输入数字')
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for q in range(10):
#         if str(q)==j:
#             q=q*10**i
#             s=s+q
# print(s)
# a=input("数字")
# b=a[::-1]
# s=0
# for i,j in enumerate(b):
#     for f in range(10):
#         if str(f)==j:
#             f=f*10**i
#             s=s+f
# print(s)
# print(type(s))
#
#
# def zhengshu(a):
#     b=a[::-1]
#     c=0
#     for i,j in enumerate(b):
#         for f in range(10):
#             if str(f)==j:
#                 f=f*10**i
#                 c=c+f
#     print(c)
# zhengshu('1242342')




























