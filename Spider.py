# -*- coding=UTF-8 -*-
# @Time : 2021/8/18 16:16
# @Author : xuchuan
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行EXCEL操作
import sqlite3  # sqlite数据库操作


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\豆瓣电影TOP250.xls"
    # 3.保存数据
    # saveData(savepath)
    # askURL(baseurl)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):  # 调用获取页面信息的函数 10 次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.获取一次就解析一次数据
        soup = BeautifulSoup(html,"html.parser")
        itemlist=soup.find_all('div',class_="item")
        for item in itemlist:
            item=str(item)
            link = re.findall('<a href="(.*?)">',item)[0]
            print(link)
    return datalist


# 得到指定一个URL的网页内容
def askURL(url):
    # 告诉网站服务器我们是什么类型的浏览器，本质上是告诉服务器我们可以接收什么水平的文件内容
    head = {  # 模拟浏览器头部信息向服务器发送消息
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36 Edg/92.0.902.73"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


# 3.保存数据
def saveData(savepath):
    pass


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
