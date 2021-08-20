# -*- coding=UTF-8 -*-
# @Time : 2021/8/18 16:16
# @Author : xuchuan
# @Software : PyCharm

from bs4 import BeautifulSoup  # 网页解析获取数据
import re  # 正则表达式，进行文字匹配
import urllib.request, urllib.error  # 制定URL，获取网页数据
import xlwt  # 进行EXCEL操作
import sqlite3  # sqlite数据库操作

# 影片数据抓取规则
finaLink = re.compile('<a href="(.*?)">')  # 每个列表里的A标签链接
# 影片图片
findImgSrc = re.compile('<img.*src="(.*?)"', re.S)  # re.S让换行符包含在字符中
# 影片片名
fingTitle = re.compile('<span class="title">(.*)</span>')
# 评分
findScore = re.compile('<span class="rating_num" property="v:average">(.*)</span>')
# 评价人数
findJudge = re.compile('<span>(\d*)人评价</span>')
# 概况
findInq = re.compile('<span class="inq">(.*)</span>')
# 影片相关内容
findBd = re.compile('<p class="">(.*?)</p>', re.S)


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = "豆瓣电影TOP250.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    # askURL(baseurl)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 10):  # 调用获取页面信息的函数 10 次
        url = baseurl + str(i * 25)
        html = askURL(url)  # 保存获取到的网页源码
        # 2.获取一次就解析一次数据
        soup = BeautifulSoup(html, "html.parser")
        for item in soup.find_all('div', class_='item'):
            data = []
            item = str(item)

            Link = re.findall(finaLink, item)[0]
            data.append(Link)

            ImgSrc = re.findall(findImgSrc, item)[0]
            data.append(ImgSrc)

            Title = re.findall(fingTitle, item)
            if (len(Title) == 2):
                cTitile = Title[0]  # 添加中文名
                data.append(cTitile)
                oTitle = Title[1].replace("/", "")  # 去掉/
                data.append(oTitle)  # 添加外语名
            else:
                data.append(Title[0])
                data.append(' ')  # 外语名留空

            Score = re.findall(findScore, item)[0]
            data.append(Score)

            Judge = re.findall(findJudge, item)[0]
            data.append(Judge)

            Inq = re.findall(findInq, item)
            if len(Inq) != 0:
                Inq = Inq[0].replace(".", "")  # 去掉句号
                data.append(Inq)
            else:
                data.append(" ")

            Bd = re.findall(findBd, item)[0]
            Bd = re.sub(r"<br(\s+)?/>(\s+)?", " ", Bd)  # 去掉br
            Bd = re.sub("/", " ", Bd)  # 替换/
            data.append(Bd.strip())  # 去掉前后的空格
            datalist.append(data)  # 把处理好的一部电影信息放入datalist

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
def saveData(datalist, savepath):
    book = xlwt.Workbook(encoding="utf-8",style_compression=0)  # 创建workbook对象
    sheet = book.add_sheet("豆瓣电影Top250", cell_overwrite_ok=True)  # 创建工作表
    col = ('电影详情链接', '图片链接', '影片中文名', '影片外文名', '评分', '评价人数', '电影概况', '相关信息')
    for i in range(0, 8):
        sheet.write(0, i, col[i])
    for i in range(0, 250):
        print("第%d条" % (i + 1))
        data = datalist[i]
        for j in range(0, 8):
            sheet.write(i + 1, j, data[j])

    book.save(savepath)  # 保存表


if __name__ == "__main__":  # 当程序执行时
    # 调用函数
    main()
    print("爬取完毕!")
