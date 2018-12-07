def shuzi(a):
    for i in a:
        for j in a:
            for h in a:
                if i !=j and j!=h and h !=i:
                    print((i+j*10+h*100))
shuzi([2,3,4,5])
# a=input('>>>')
# b=a.split()
# c=[]





# for i in b:
#     for j in b:
#         for h in b:
#             if (i != j) and (i != h) and (j != h):
#                 print(i,j,h)
#                 c.append(int(i)*100+int(j)*10+int(h))
# print(c)


