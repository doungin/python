# import json
# data={'姓名': 12}
# data1=json.dumps(data)
# data2=json.loads(data1)
# print(data2['姓名'])


# def maopao(x):
#     for i in range(len(x)-1):
#         for j in range(len(x)-i-1):
#             if x[j] > x[j+1]:
#                 x[j],x[j+1]=x[j+1],x[j]     ## 冒泡排序，用函数
#     print(x)
#
#
# maopao([1,5,6,7,2,4,9,7,3,5,5,8,9,3,7,6,8])





# import requests
# import re
# def wangzhi():
#     url='https://book.douban.com/latest?icn=index-latestbook-all'
#     head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#     res=requests.get(url=url,headers=head)
#     html=res.content.decode('utf-8')
#     return html
# def jieguo(a):
#     head = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
#     patt=re.compile('<img src="(.*?)"/></a>')
#     items=patt.findall(a)
#     print(items)
#     for j,i in enumerate(items):
#         new_url=i
#         respons=requests.get(url=new_url,headers=head)
#         tu=respons.content
#         with open(r'C:\Users\doungin\Desktop\新建文件夹\新建文件夹\{}.jpg'.format(j+1),'wb') as f:
#             f.write(tu)
# b=wangzhi()
# jieguo(b)





#
# import requests
# import re
# class Qingqiu():
#     def qingqiu(self,page):
#         url='http://www.17k.com/chapter/2899153/{}.html'.format(page)
#         aaa=requests.get(url=url)
#         html = aaa.content.decode('utf-8')
#         # print(html)
#         return html
#     def guolv(self,html):
#         shuju=[]
#         patt=re.compile('<span class="ellipsis">(.*?)</a>',re.S)
#         htmll=patt.findall(html)
#         print(htmll)
#         for i in htmll:
#             i = i.replace('<span>', '')
#             i = i.replace('</span>', '')
#             i = i.replace('&#12288;&#12288;','')
#             i = i.replace('<br /><br />', '\n')
#             i = i.strip()
#             shuju.append(i)
#         return shuju
#     def save(self,shuju):
#         with open('a.txt','a',encoding='utf-8') as f:
#             for i in shuju:
#                 print(i)
#                 f.write(i)
# qiushi=Qingqiu()
# jieguo=qiushi.qingqiu(35985504)
# shuju=qiushi.guolv(jieguo)
# qiushi.save(shuju)
# a=[23,34,54,12,43]
# b=a.copy()
# for i in range(len(b)):
#     for j in range(i,len(b)):
#         if b[i]>b[j]:
#             b[i],b[j]=b[j],b[i]
# c=a.index(b[0])
# d=a.index(b[-1])
# a[c],a[0]=a[0],a[c]
# a[d],a[-1]=a[-1],a[d]
# print(a)
# if __name__=='__main__':
def liebie(a):
    b=[]
    for i in a:
        if i not in b:
            b.append(i)
    b.sort()
    print(b[0],b[-1])
liebie([21,32,43,564,23])
