#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
from selenium import webdriver
import xlwt
from bs4 import BeautifulSoup
import re
from html.parser import HTMLParser
import html
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
        self.data_types = set()
        self.fields = set()
        # self.html_parser = HTMLParser()

    @staticmethod
    def clean_p_html(ps):
        if len(ps) > 1:
            p_texts = []
            for p in ps:
                p_text = p.text.strip()
                p_text = re.sub('\n', '', p_text)
                p_text = re.sub(' {2,}', ' ', p_text)
                p_texts.append(p_text)
            text = '\n'.join(p_texts)
        else:
            p_text = ps[0].text.strip()
            p_text = re.sub('\n', '', p_text)
            p_text = re.sub(' {2,}', ' ', p_text)
            text = p_text

        text = re.sub(u'\xa0', ' ', text)
        # text = self.html_parser.unescape(text)
        # 转义html中的特殊字符，形如&nbsp
        # text = html.unescape(text)

        return text

    def parse_table(self, table, section_title, table_title):
        log_template = None
        variable_fields = None
        log_example = None
        log_desc = None
        data_type = None
        log_explanation = None
        log_recommended_action = None
        fields = None

        table_rows = table.find_all('tr')

        for row in table_rows:
            tds = row.find_all('td')
            table_head = tds[0].text.strip()
            if table_head == "日志内容":
                # log_template = tds[1].text.strip()
                ps = tds[1].find_all('p')
                text = self.clean_p_html(ps)
                log_template = text
                print("日志模板:\n{}".format(log_template))
                data_type = re.findall('\[[^\[]*?\]', log_template)
                data_type = set(data_type)

            if table_head == "参数解释":
                params = []
                fields = set()
                ps = tds[1].find_all('p')
                for p in ps:
                    param = p.text.strip()
                    # params.append(param)
                    if re.search('\$\d.*', param):
                        field = re.sub('.*[\$\d:：\|]', '', param).strip()
                        fields.add(field)

                    params.append(param)

                variable_fields = '|'.join(params)
                print("参数解释:\n{}".format(variable_fields))

            if table_head == "举例":
                # log_example = tds[1].text.strip()

                ps = tds[1].find_all('p')
                text = self.clean_p_html(ps)
                log_example = text
                print("举例:\n{}".format(log_example))

                # 模块标识
                # TODO:类似SNMP中的SNMP_NOTIFY
                log_desc = log_example.split(":")[0]
                # log_desc = log_desc.replaceAll("(\s[\u4E00-\u9FA5]+)|([\u4E00-\u9FA5]+\s)", "")
                log_desc = re.findall('[a-zA-Z0-9]+', log_desc)
                print("模块标识:\n{}".format(log_desc))

            if table_head == "日志说明":
                ps = tds[1].find_all('p')

                text = self.clean_p_html(ps)
                log_explanation = text

                # log_explanation = tds[1].text.strip()
                print("日志说明:\n{}".format(log_explanation))

            if table_head == "处理建议":
                # log_recommended_action = tds[1].text.strip()
                ps = tds[1].find_all('p')
                text = self.clean_p_html(ps)
                log_recommended_action = text
                print("处理建议：\n{}".format(log_recommended_action))

        # if data_type not in self.data_types:
        if data_type:
            self.data_types |= data_type

        if fields:
            self.fields |= fields

        if log_template in self.result:
            print("日志内容重复,原日志案例为{},现日志案例为{}".format(self.result[log_template], log_example))

        log_name = section_title + table_title

        self.result[log_template] = (log_desc, variable_fields, log_example,
                                     log_explanation, log_recommended_action, log_name)

    def parse_log_html_cn(self, html):
        soup = BeautifulSoup(html, "html.parser")

        section = soup.find('div', _class='WordSection1')
        section_title = ''
        table_title = ''
        for s in section:
            tag = s.tag
            if tag == 'h1':
                section_title = s.text.strip()
            elif tag == 'h2':
                log_name = s.text.strip()
            elif tag == 'table':
                s_class = s['class']
                if s_class == 'Tablenohead0':
                    self.parse_table(s, section_title, table_title)













        # 获得log表格信息的panel
        log_tables = soup.find_all('table')

        for table in log_tables:
            # contents = table.contents
            print('---------------------------')





        return self.result

    def parse_log_html_en(self, html):
        soup = BeautifulSoup(html, "html.parser")
        # 获得log表格信息的panel
        log_tables = soup.find_all('table')

        for table in log_tables:
            # contents = table.contents
            print('---------------------------')

            log_template = None
            variable_fields = None
            log_example = None
            log_desc = None
            data_type = None
            log_explanation = None
            log_recommended_action = None

            table_rows = table.find_all('tr')

            for row in table_rows:
                tds = row.find_all('td')
                table_head = tds[0].text.strip()
                if table_head == "Message text":
                    # log_template = tds[1].text.strip()
                    ps = tds[1].find_all('p')
                    text = self.clean_p_html(ps)
                    log_template = text
                    print("日志模板:\n{}".format(log_template))
                    data_type = re.findall('\[[^\[]*?\]', log_template)
                    data_type = set(data_type)

                if table_head == "Variable fields":
                    params = []
                    ps = tds[1].find_all('p')
                    for p in ps:
                        param = p.text.strip()
                        params.append(param)

                    variable_fields = '|'.join(params)
                    print("参数解释:\n{}".format(variable_fields))

                if table_head == "Example":
                    # log_example = tds[1].text.strip()

                    ps = tds[1].find_all('p')
                    text = self.clean_p_html(ps)
                    log_example = text
                    print("举例:\n{}".format(log_example))

                    # 模块标识
                    log_desc = log_example.split(":")[0]
                    print("模块标识:\n{}".format(log_desc))

                if table_head == "Explanation":
                    ps = tds[1].find_all('p')

                    text = self.clean_p_html(ps)
                    log_explanation = text

                    # log_explanation = tds[1].text.strip()
                    print("日志说明:\n{}".format(log_explanation))

                if table_head == "Recommended action":
                    # log_recommended_action = tds[1].text.strip()
                    ps = tds[1].find_all('p')
                    text = self.clean_p_html(ps)
                    log_recommended_action = text
                    print("处理建议：\n{}".format(log_recommended_action))
            if data_type:
                self.data_types |= data_type

            # if log_template in self.result:
            #     print("日志内容重复,原日志案例为{},现日志案例为{}".format(self.result[log_template], log_example))
            self.result[log_template] = (log_desc, variable_fields, log_example,
                                         log_explanation, log_recommended_action)

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
            self.parse_log_html_cn(html)
            # result_page += result_module

            self.driver.back()

    def one_page_h3c_press_en(self):
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

            if file_name == "Introduction":
                continue

            print("正在抓取 {} 模块日志".format(file_name))
            # self.driver.find_element_by_xpath(tl).click()
            self.driver.find_element_by_link_text(file_name).click()
            html = self.driver.page_source
            self.parse_log_html_en(html)
            # result_page += result_module

            self.driver.back()

    def run(self, saved_path, lang='zh'):
        self.driver.get(self.site)

        ui.WebDriverWait(self.driver, 10)

        time.sleep(3)

        while True:
            if lang == 'zh':
                self.one_page_h3c_press()
            else:
                self.one_page_h3c_press_en()

            try:
                self.driver.find_element_by_link_text("下一页")
            except Exception as e:
                print(e)
                break

            self.driver.find_element_by_link_text("下一页").click()

            windows = self.driver.window_handles
            self.driver.switch_to.window(windows[-1])

        print("共有 {} 种日志模板".format(len(self.result)))

        # 创建一个Workbook对象，相当于创建了一个Excel文件
        book = xlwt.Workbook(encoding="utf-8", style_compression=0)

        # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
        sheet = book.add_sheet('test01', cell_overwrite_ok=True)
        # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

        print("变量数据类型包含:{}\n".format(self.data_types))
        print("参数字段共有{}种\n包含:{}\n".format(len(self.fields), self.fields))

        for i, (k, v) in enumerate(self.result.items()):
            sheet.write(i, 0, k)
            sheet.write(i, 1, v[0])
            sheet.write(i, 2, v[1])
            sheet.write(i, 3, v[2])
            sheet.write(i, 4, v[3])
            sheet.write(i, 5, v[4])

        book.save(saved_path)


if __name__ == '__main__':
    spider = LogSpider("http://press.h3c.com/jsp/ir/fileList.do?classID=202&fileID=498533")
    spider.run(saved_path='files/result_0706_cn.xls')

    # spider = LogSpider("http://press.h3c.com/jsp/ir/fileList.do?classID=302&fileID=497167")
    # spider.run(saved_path='files/result_0706_en.xls', lang='en')

