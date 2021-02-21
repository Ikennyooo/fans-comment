import urllib.request
from bs4 import BeautifulSoup
import random
import time



def getRequest(url):
    # 分多个浏览器访问豆瓣网，防止访问多页时被拒绝
    header1 = {
        "Host": "movie.douban.com",
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36 Edg/88.0.705.74",
        "Cookie": 'bid=as_ISkW5p6o; douban-fav-remind=1; __yadk_uid=UdDpByaph01pXE2HQBN1Q8EXMVKQRiSS; ll="118204"; _vwo_uuid_v2=D2251C090BDECE79EA55F6486697C0016|5dfc67bb3150e39951e24faa031ae772; __utmc=30149280; __utmc=223695111; push_doumail_num=0; push_noty_num=0; __utmv=30149280.21255; _pk_ref.100001.4cf6=%5B%22%22%2C%22%22%2C1613883142%2C%22https%3A%2F%2Faccounts.douban.com%2F%22%5D; _pk_ses.100001.4cf6=*; __utma=30149280.1347028292.1612620418.1613846158.1613883142.10; __utmz=30149280.1613883142.10.3.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; __utma=223695111.899026902.1613705049.1613846158.1613883142.7; __utmb=223695111.0.10.1613883142; __utmz=223695111.1613883142.7.2.utmcsr=accounts.douban.com|utmccn=(referral)|utmcmd=referral|utmcct=/; dbcl2="212556088:1A9lPn3a0aE"; ck=DGv0; __utmt=1; douban-profile-remind=1; __gads=ID=c5ad8890250c1ec6-2222ab9af2c500d7:T=1612620417:S=ALNI_MbRwK7aja0PHi8zCpSRrNZtqrgHsw; __utmb=30149280.36.10.1613883142; _pk_id.100001.4cf6=c3bc4b8688b36120.1613705048.7.1613883585.1613846395.'
    }
    # 将浏览器装入列表里
    list = [header1]
    # 随机取一个请求头  len(list)-1：列表长度-1
    index = random.randint(0, len(list)-1)
    # 随机用一个请求头，开始访问地址
    req = urllib.request.Request(url=url, headers=list[index])
    # 返回结果~
    return req


# 封装函数，爬取数据
def getData(url,commentAll):
    try:
        # 获取处理后的请求
        req = getRequest(url)
        # 打开网址
        html = urllib.request.urlopen(req)
        # 读取数据(data得到所有数据)
        data = html.read()
        # print(data)
        # 定义soup对象，解析网页
        soup = BeautifulSoup(data, "html.parser")
        # 找到装有所有评论的id名为comments的div
        # ["数据"]  数组里只有一个元素----数据
        comments = soup.select("#content")[0]
        # print(comments)
        # 读取到每一条评论，div的class名为comment-item
        items = comments.select(".name")
        # print(items)
        # 循环遍历每一条评论
        for i in items:
            author = i.string
            # 将 用户名装入在字典里面
            commentAll.append(author)
    except:
        pass

    return commentAll



# 把数据弄到列表中的函数
def writeInto(commentAll):
    all = []
    all.append(commentAll)
    return all


if __name__ == '__main__':
    # 初始化一个空列表,将得到的所有数据
    commentAll = []
    nihao = []
    cisha = []
    tangren = []

    # range()产生序列 0.1.2,爬取3页
    for i in range(0, 270):
        # 爬取的网页地址280
        # 找出规律，改掉start的数字就行
        url = "https://movie.douban.com/subject/34841067/reviews?start=%d"%(i*20)
        # 调用函数，爬取数据 nihaolihuanying
        if i >= 5580:
            break
        getData(url, commentAll)
        nihao = writeInto(commentAll)
        # 每爬取一个页面数据，休息10秒，防止被封号
        time.sleep(10)
    # 调用函数，爬取完数据，装入表格
    print(nihao)
    commentAll = []

    for j in range(0, 130):
        # 爬取的网页地址137
        # 找出规律，改掉start的数字就行
        url = "https://movie.douban.com/subject/26826330/reviews?start=%d"%(j*20)
        # 调用函数，爬取数据 cishaxiaoshuojia
        if j >= 2720:
            break
        getData(url, commentAll)
        cisha = writeInto(commentAll)
        # 每爬取一个页面数据，休息10秒，防止被封号
        time.sleep(10)
    # 调用函数，爬取完数据，装入表格
    print(cisha)
    commentAll = []


    for k in range(0, 300):
        # 爬取的网页地址322
        # 找出规律，改掉start的数字就行
        url = "https://movie.douban.com/subject/27619748/reviews?start=%d"%(k*20)
        if k >= 6420:
            break
        # 调用函数，爬取数据 tangrenjietanan3
        getData(url, commentAll)
        tangren = writeInto(commentAll)
        # 每爬取一个页面数据，休息10秒，防止被封号
        time.sleep(10)
    print(tangren)
    commentAll = []

    num1 = 0
    chong12 = [val for val in nihao if val in cisha]
    chong3 = [val for val in nihao if val in cisha if val in tangren]

    print("三部影片影评的重合的用户:")
    for it in chong3:
        num1 += 1
        print(it, end=" ")
    print("")
    print("三部影片影评的用户重合数：" + str(num1))

    rate = len(chong3)/(3*len(nihao)-2*len(chong3))
    print("三部影片影评的用户重合度：" + str(rate*100) + "%")