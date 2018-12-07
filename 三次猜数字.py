# import random
# a=random.randrange(1,10)
# while a < 10:
#     b = int(input("请输入一个数字"))
#     if b > a:
#      print('大了')
#     if a > b:
#      print('小了')
#     if b==a:
#      print("对了")



import random
a=random.randrange(1,10)
for i in range(0,3,1):
    b = int(input("请输入一个数字"))
    if b == a:
        print("正确")
        break
    if b>a:
        print('大了')
        print("你还有{}次机会".format(2-i))
    if b<a:
        print('小了')
        print('你还有{}次机会'.format(2-i))
else:
    print("笨蛋")

