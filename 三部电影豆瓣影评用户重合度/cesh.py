# -*- codeing = utf-8 -*-
# -*- codeing = UTF-8 -*-
# @Time : 2021/2/21 0:28
# @Author : Ikennyooo
# @File : cesh.py
# @Software: PyCharm
import urllib.request
from bs4 import BeautifulSoup
import random
import time

def getRequest(url):
    # 分多个浏览器访问豆瓣网，防止访问多页时被拒绝
    header1 = {
        "Host": "movie.douban.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
        "Cookie": 'bid=as_ISkW5p6o; douban-fav-remind=1; __gads=ID=c5ad8890250c1ec6-2222ab9af2c500d7:T=1612620417:RT=1612620417:S=ALNI_MbRwK7aja0PHi8zCpSRrNZtqrgHsw; __utmz=30149280.1612701553.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1613705049.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=UdDpByaph01pXE2HQBN1Q8EXMVKQRiSS; ll="118204"; _vwo_uuid_v2=D2251C090BDECE79EA55F6486697C0016|5dfc67bb3150e39951e24faa031ae772; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmv=30149280.21255; _pk_ses.100001.4cf6=*; __utma=30149280.1347028292.1612620418.1613828110.1613836944.7; __utma=223695111.899026902.1613705049.1613828110.1613836944.4; __utmb=223695111.0.10.1613836944; ap_v=0,6.0; __utmt=1; __utmb=30149280.7.10.1613836944; dbcl2="212556088:vqUIxjA5Fdg"; ck=iWow; _pk_id.100001.4cf6=c3bc4b8688b36120.1613705048.4.1613837114.1613834867.'
    }
    header2 = {
        "Host": "movie.douban.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0",
        "Cookie": 'bid=as_ISkW5p6o; douban-fav-remind=1; __gads=ID=c5ad8890250c1ec6-2222ab9af2c500d7:T=1612620417:RT=1612620417:S=ALNI_MbRwK7aja0PHi8zCpSRrNZtqrgHsw; __utmz=30149280.1612701553.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1613705049.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=UdDpByaph01pXE2HQBN1Q8EXMVKQRiSS; ll="118204"; _vwo_uuid_v2=D2251C090BDECE79EA55F6486697C0016|5dfc67bb3150e39951e24faa031ae772; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmv=30149280.21255; _pk_ses.100001.4cf6=*; __utma=30149280.1347028292.1612620418.1613828110.1613836944.7; __utma=223695111.899026902.1613705049.1613828110.1613836944.4; __utmb=223695111.0.10.1613836944; ap_v=0,6.0; __utmt=1; __utmb=30149280.7.10.1613836944; dbcl2="212556088:vqUIxjA5Fdg"; ck=iWow; _pk_id.100001.4cf6=c3bc4b8688b36120.1613705048.4.1613837114.1613834867.'
    }
    header3 = {
        "Host": "movie.douban.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3100.0 Safari/537.36",
        "Cookie": 'bid=as_ISkW5p6o; douban-fav-remind=1; __gads=ID=c5ad8890250c1ec6-2222ab9af2c500d7:T=1612620417:RT=1612620417:S=ALNI_MbRwK7aja0PHi8zCpSRrNZtqrgHsw; __utmz=30149280.1612701553.2.2.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; __utmz=223695111.1613705049.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __yadk_uid=UdDpByaph01pXE2HQBN1Q8EXMVKQRiSS; ll="118204"; _vwo_uuid_v2=D2251C090BDECE79EA55F6486697C0016|5dfc67bb3150e39951e24faa031ae772; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmv=30149280.21255; _pk_ses.100001.4cf6=*; __utma=30149280.1347028292.1612620418.1613828110.1613836944.7; __utma=223695111.899026902.1613705049.1613828110.1613836944.4; __utmb=223695111.0.10.1613836944; ap_v=0,6.0; __utmt=1; __utmb=30149280.7.10.1613836944; dbcl2="212556088:vqUIxjA5Fdg"; ck=iWow; _pk_id.100001.4cf6=c3bc4b8688b36120.1613705048.4.1613837114.1613834867.'
    }
    # 将浏览器装入列表里
    list = [header1, header2, header3]
    # 随机取一个请求头  len(list)-1：列表长度-1
    index = random.randint(0, len(list)-1)
    # 随机用一个请求头，开始访问地址
    req = urllib.request.Request(url=url, headers=list[index])
    # 返回结果~
    return req


req = getRequest("https://movie.douban.com/subject/34841067/reviews?start=%d")
# 打开网址
html = urllib.request.urlopen(req)
# 读取数据(data得到所有数据)
data = html.read()
# 输出爬取到的所有数据，进制形式显示
# print(data)
# 定义soup对象，解析网页
soup = BeautifulSoup(data,"html.parser")
# 找到装有所有评论的id名为comments的div
# ["数据"]  数组里只有一个元素----数据
comments = soup.select("#content")[0]
# print(comments)
# 读取到每一条评论，div的class名为comment-item
items = comments.select(".name")
# print(items)
# 循环遍历每一条评论
for i in items:
    print(i.string)

num1 = 1
print("s",end=" ")
print("")
print("三部影片影评的用户重合数："+ str(num1))