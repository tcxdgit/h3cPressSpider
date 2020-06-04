#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver
import xlwt
from bs4 import BeautifulSoup

import selenium.webdriver.support.ui as ui

js = "var q=document.body.scrollTop=10000"  # documentElement表示获取body节点元素


class LogSpider(object):
    def __init__(self, site="http://press.h3c.com/portal/release/ir/default.jsp?classID=202"):
        # 用chrome驱动
        chrome_driver = r"D:\Program Files\chromedriver.exe"
        self.driver = webdriver.Chrome(executable_path=chrome_driver)
        # self.driver.get(site)
        self.site = site
        self.result = {}

    def parse_log_html(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 获得log表格信息的panel
        log_tables = soup.find_all('table')

        for table in log_tables:
            # contents = table.contents

            log_template = None
            log_example = None

            table_rows = table.find_all('tr')

            for row in table_rows:
                tds = row.find_all('td')
                table_head = tds[0].text.strip()
                if table_head == "日志内容":
                    log_template = tds[1].text.strip()
                    print("日志内容:\n{}".format(log_template))

                if table_head == "举例":
                    log_example = tds[1].text.strip()
                    print("日志举例:\n{}".format(log_example))

            self.result[log_template] = log_example

        return self.result

    def one_page_h3c_press(self):
        # result_page = {}

        xpath_locator = '//*[@id="tbsort"]'
        print()


        # 获取行数，除去表头
        table_tr = self.driver.find_elements_by_xpath(xpath_locator + "/tbody/tr")[1:]
        row = len(table_tr)

        # 根据行列数遍历table中的所有文本，并获取匹配的文本所在的行列
        for i in range(2, row + 2):
            tl = xpath_locator + "/tbody/tr[" + str(i) + "]/td[1]"
            file_name = self.driver.find_element_by_xpath(tl).text  # 获取模块名称

            if file_name == "简介":
                continue

            print("正在抓取 {} 模块日志".format(file_name))
            # self.driver.find_element_by_xpath(tl).click()
            self.driver.find_element_by_link_text(file_name).click()
            html = self.driver.page_source
            self.parse_log_html(html)
            # result_page += result_module

            self.driver.back()

        # return result_page

    def run(self):
        self.driver.get(self.site)

        ui.WebDriverWait(self.driver, 10)

        time.sleep(3)

        while True:

            self.one_page_h3c_press()
            try:
                self.driver.find_element_by_link_text("下一页")
            except Exception as e:
                print(e)
                break

            # if next_page:

            self.driver.find_element_by_link_text("下一页").click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])

        print("共有 {} 种日志模板".format(len(self.result)))

        # 创建一个Workbook对象，相当于创建了一个Excel文件
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)

        # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
        sheet = book.add_sheet('test01', cell_overwrite_ok=True)
        # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

        for i, (template, example) in enumerate(self.result.items()):
            sheet.write(i, 0, template)
            sheet.write(i, 1, example)

        book.save('test1.xls')


if __name__ == '__main__':
    spider = LogSpider("http://press.h3c.com/jsp/ir/fileList.do?classID=202&fileID=488813")
    spider.run()

