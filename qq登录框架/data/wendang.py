#！/usr/bin/env python
# -*- encoding:utf-8 -*-
import xlrd
class duqu():
    def shuju(self):
        dd=[]
        f=xlrd.open_workbook(r'D:\新建文件夹\doungin\新建文件夹\qq登录框架\data\1233.xlsx')
        sheet=f.sheets()[0]
        bb=sheet.nrows
        for i in range(bb):
            cc=sheet.row_values(i)
            dd.append(cc)
        ff=[]
        for i in dd:

            if type(i[0])==float:
                i[0]=int(i[0])
                # ff.append(i)
                if type(i[1])==float:
                    i[1]=int(i[1])
                    ff.append(i)
                else:
                    ff.append(i)
        return ff
# aa=duqu()
# bb=aa.shuju()
#
# for i in bb:
#     print(i)
