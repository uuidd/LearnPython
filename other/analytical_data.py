#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
脚本环境建构
安装python
新建一个文件夹
将附件1.xlsx（请勿改名）复制到该文件夹中，保证附件1与脚本属于同个文件夹中
按住shift键右键打开在【此处打开 Powershell窗口】
输入pip install openpyxl，安装openpyxl库
运行该脚本，耐心等待，所生成文件将在文件夹中出现
运行脚本时，请先关闭所有excel文件，重复执行脚本，生成的文件将直接被覆盖
"""

from openpyxl import Workbook, load_workbook


def create_table():
    """
    创建excel文件
    """
    new_excel = Workbook()
    new_sheet = new_excel.active
    new_sheet.title = "Sheet0"
    header = ["证券代码", "证券名称", "交易时间", "开盘价", "最高价", "最低价", "收盘价", "涨跌", "涨跌幅%", "成交量", "成交额", "盘后量", "盘后额"]
    new_sheet.append(header)  # 添加首列标题
    new_sheet.column_dimensions["C"].width = 20  # 设置交易时间的列宽，防止显示"#####"
    print("Reading data...Please wait！")
    data_list = sorted(read_data("附件1.xlsx"), key=lambda x: x[2])  # 数据根据时间排序
    for column_list in data_list:
        print(column_list)
        new_sheet.append(column_list)  # 向表格中导入数据
    print("Saving...")
    new_excel.save("StockData.xlsx")
    print("Complete!")


def read_data(file_name):
    """
    读取excel数据
    :param file_name: 文件名
    :return: 二维列表
    """
    original_table = load_workbook(filename=file_name)  # 读取excel文件数据
    sheets_name = original_table.sheetnames  # 获取所有sheet表名字
    data_list = []
    for i in sheets_name:
        ws = original_table[i]
        max_row = ws.max_row  # 获取该sheet的最大行数
        max_column = ws.max_column  # 获取该sheet的最大列数
        for row in range(2, max_row-5):
            column_list = []  # 跳过首列标题，从第二行开始读取数据，删除最后空了的五行
            for col in range(1, max_column+1):
                data = ws.cell(row=row, column=col).value
                if data == "——":
                    data = 0
                column_list.append(data)
            data_list.append(column_list)

    return data_list


if __name__ == '__main__':
    create_table()
