# -*- coding=UTF-8 -*-
# @Time : 2021/8/19 17:18
# @Author : xuchuan
# @Software : PyCharm

# 正则表达式：字符串模式（判断字符串是否符合一定的标准）
import re

# 创建模式对象
# pat = re.compile("AA")  # 此处设置正则表达式为AA，用来验证其他的字符串
# m = pat.search("CBA")  # search里的字符串是被校验的内容
# m = pat.search("CBAA")
# m = pat.search("AACBAAAAA")  # search进行查找比对

# 没有模式对象
# m = re.search("asd","Aasd")  #前面是规则，后面内容是查找对象
# print(m)


# print(re.findall("a","ASDFGHaDFa"))  #前面是规则，后面是被校验的字符串，返回所有符合规则的内容列表
# print(re.findall("[A-Z]","ASDFGHaDFa"))  #前面是规则，后面是被校验的字符串，返回所有符合规则的内容列表
# print(re.findall("[A-Z]+", "ASDFGHaDFa"))

# sub
print(re.sub("a", "A", "asdfasdfsd"))  # 找到a,用A替换，在第三个字符串内容找

# 建议在正则表达式中，被比较的字符串前面加上r，不用担心转义字符的问题
