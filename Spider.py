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
    saveData(savepath)


# 爬取网页
def getData(baseurl):
    datalist = []
    # 2.逐一解析数据
    return datalist


# 3.保存数据
def saveData(savepath):
    pass


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
