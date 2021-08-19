# -*- coding=UTF-8 -*-
# @Time : 2021/8/19 10:39
# @Author : xuchuan
# @Software : PyCharm

# Tag
# NavigableString
# BeautifuSoup
# Comment  :是一个特殊的NavigableString类型，输出的内容不包含注释符号
import re

from bs4 import BeautifulSoup

file = open("./douban.html", "rb")  # 读取为二进制形式
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")
# print(bs.title)
# print(bs.a)
# print(bs.head)
# 1.Tag对象： 存储css标签及标签中内容为tag对象：取所找到的第一个内容

# print(bs.title.string)
# 2.NavigableString对象： 标签里的内容（字符串）

# print(bs.a.attrs)  #拿到标签属性

# print(type(bs))
# 3.BeautifulSoup对象：整个文档

# print(bs)


# print(type(bs.a.string))


# --------------------------如何应用------------------

# 文档的遍历
# print(bs.head.contents)
# print(bs.head.contents[1])
# 更多内容，搜索BeautifuSoup文档

# 文档的搜索
# 1.find_all()
# 字符串过滤：查找与字符串完全匹配的内容
# t_list = bs.find_all("a")

# 正则表达式搜索：search()方法来匹配内容
t_list = bs.find_all(re.compile("a"))

# 方法搜索： 传入函数（方法），根据函数的要求来搜索
# def name_is_exists(tag):
#     return tag.has_attr("name")
# t_list=bs.find_all(name_is_exists)
#
# for item in t_list:
#     print(item)

# 2.kwargs  参数
# t_list = bs.find_all(class_=True)
# for item in t_list:
#     print(item)

# 3.text参数
# t_list = bs.find_all(text=["肖申克的救赎","控方证人"])
# t_list = bs.find_all(text=re.compile("\d"))  #正则表达式查找包含特定文本的内容（标签里的字符串）


# 4.limit参数
# t_list = bs.find_all("a", limit=3)
# for item in t_list:
#     print(item)

# css选择器
# print(bs.select('title'))   #通过标签来查找
# t_list=bs.select(".title")  #通过类名查找
# t_list =bs.select("#u1")  #通过ID查找
# t_list =bs.select("a[class='']")  #通过属性查找
# t_list = bs.select("head > title")  # 通过子标签查找
t_list = bs.select(".title ~.bri")
for i, item in enumerate(t_list):
    print(i + 1, item)
