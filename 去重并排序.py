# def quchong(b):
#     for i in b:
#         if b.count(i)>1:
#             for f in range(b.count(i)-1):
#                 b.remove(i)
#     b.sort()
#     print(b)
# quchong([2,2,32,23,43,32])
def quchong(a):
    for i in a:
        if a.count(i)>1:
            for j in range(a.count(i)-1):
                a.remove(i)
    b = len(a)
    for i in range(b - 1):
        for j in range(b - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
    print(a)
quchong([12,32,12,32,4345,432,23,23])















