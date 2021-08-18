# -*- coding=UTF-8 -*-
# @Time : 2021/8/18 17:27
# @Author : xuchuan
# @Software : PyCharm

import urllib.request

response = urllib.request.urlopen("http://www.baidu.com")
print(response.read().decode('utf-8'))
