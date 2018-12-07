import xlrd

def duqu():
    shuju = []
    f = xlrd.open_workbook(r'D:\新建文件夹\doungin\新建文件夹\app框架\date\test数据.xlsx')
    sheet = f.sheets()[0]
    num = sheet.nrows
    for i in range(1,num):
        shuju.append(sheet.row_values(i))
    return shuju

def duqu1():
    with open(r'D:\新建文件夹\doungin\新建文件夹\app框架\date\run.txt','r') as f:
        shuju = f.readlines()
    return shuju



if __name__ == '__main__':
    print(duqu())
