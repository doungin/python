a=0
for i in range(1,10):
    for j in range(1,i+1):
        a=i*j
        print("{}*{}={}".format(i,j,a),end="\t")
    print()