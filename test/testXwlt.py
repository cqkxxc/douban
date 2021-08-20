# -*- coding=UTF-8 -*-
# @Time : 2021/8/20 15:21
# @Author : xuchuan
# @Software : PyCharm

import xlwt

workbook = xlwt.Workbook(encoding="utf-8")  # 创建workbook对象
worksheet = workbook.add_sheet("sheet1")  # 创建工作表
# worksheet.write(0, 0, "hello")  # 写入数据，第一个参数表示行，第二个参数表示列，第三个是内容

for i in range(1, 10):
    print("\t")
    for j in range(1, i + 1):
        print("%d × %d=%d" % (i, j, i * j), end='\t')
        worksheet.write(i-1, j-1, "%d × %d=%d" % (i, j, i * j))

workbook.save("Student.xls")  # 保存表
