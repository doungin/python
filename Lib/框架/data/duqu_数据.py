#!/usr/bin/env  python
#-*- coding:utf-8 -*-
import xlrd
def tes_数据():
    shuju=[]
    f=xlrd.open_workbook(r'd:\新建文件夹\doungin\新建文件夹\123.xls')
    sheet=f.sheet_by_name('Sheet1')
    num=sheet.nrows
    for i in range(1,num):
        aaa=sheet.row_values(i)
        shuju.append(aaa)
    return shuju
# print(tes_数据())
