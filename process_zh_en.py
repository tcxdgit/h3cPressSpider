
import xlrd
import xlwt
import re
from nltk.corpus import stopwords


list_stopWords = list(set(stopwords.words('english')))


def merge_cn_en(cn_path, en_path):
    # 操作excel
    excel_cn = xlrd.open_workbook(cn_path)
    excel_en = xlrd.open_workbook(en_path)
    # excel.sheet_names()  # 获取excel里的工作表sheet名称数组
    sheet_cn = excel_cn.sheet_by_index(0)  # 根据下标获取对应的sheet表
    sheet_en = excel_en.sheet_by_index(0)  # 根据下标获取对应的sheet表

    n_rows = sheet_cn.nrows  # 获取总共的行数
    logs_cn = {}
    for row in range(n_rows):
        row_list = sheet_cn.row_values(row)    # 每一行的数据在row_list 数组里

        log_template, log_desc, variable_fields, log_example, log_explanation, log_recommended_action = row_list

        # logs_cn[log_example] = [log_template, log_desc, variable_fields, log_explanation, log_recommended_action]

        if not log_template:
            pass
        else:
            logs_cn[log_example] = {
                'log_template': log_template,
                'log_desc': log_desc,
                'variable_fields': variable_fields,
                'log_explanation': log_explanation,
                'log_recommended_action': log_recommended_action
            }

    n_rows_en = sheet_en.nrows  # 获取总共的行数
    # logs_cn = {}
    for row in range(1, n_rows_en):
        row_list = sheet_en.row_values(row)    # 每一行的数据在row_list 数组里

        _, _, variable_fields_en, log_example, _, _ = row_list

        if log_example in logs_cn:
            logs_cn[log_example]['variable_fields_en'] = variable_fields_en

    for k, v in logs_cn.items():
        log_example = k
        log_template = v['log_template']

        examples = re.findall('[0-9A-Z_]+/\d/[0-9A-Z_]+:', log_example)

        if len(examples) > 1:
            log_template = re.sub('\n', '\n或\n', log_template)

        params_template = re.findall('\[[^\[]*?\]', log_template)

        if 'variable_fields_en' in v:

            if v['log_desc'] == 'APMGR/4/APMGR_CWC_LOCAL_AC_DOWN':
                print(v)

            variable_fields_en = v['variable_fields_en']
            # variable_fields_en = re.findall('\$\d.*[\|]?', variable_fields_en)

            variable_fields_en = variable_fields_en.split('|')

            # 生成英文变量字段
            variable_fields_en_clean = []
            for e in variable_fields_en:
                if re.search('\$\d.*', e):
                    # t = re.sub('.*[\$\d:\|]', '', e)
                    t = re.sub('.*\$\d+:[\s+]?', '', e)
                    t = re.split('[.,:]', t)[0]

                    field = ''
                    for word in re.split('\s+', t):
                        word = word.strip()

                        # 去停用词
                        if word not in list_stopWords:
                            field += word.capitalize()
                    # print(v)
                    # print(field)
                    field = field[0].lower() + field[1:]
                    # t = re.sub('\s', '_', t.strip())

                    variable_fields_en_clean.append(field)

            # variable_fields_en_clean = []
            # for e in variable_fields_en:
            #     variable_fields_en_clean.append(re.sub('[\$\d:\|]', '', e))

            # print(log_template + '\n--------')
            # print(variable_fields_en_clean)
            if len(params_template) != len(variable_fields_en_clean):
                print('中英文参数不一致:\n' + log_template + '\n' + k + '\n--------------')
                for i, param in enumerate(params_template):
                    repl = param.strip(']') + ':param{}]'.format(i)
                    # 转义正则表达式中的特殊字符
                    param_escape = re.escape(param)
                    log_template = re.sub(param_escape, repl, log_template, count=1)
            else:
                # 变量字段取自英文文档
                for i, param in enumerate(params_template):

                    repl = param.strip(']') + ':' + variable_fields_en_clean[i] + ']'
                    # 转义正则表达式中的特殊字符
                    param_escape = re.escape(param)
                    log_template = re.sub(param_escape, repl, log_template, count=1)
        else:
            print('没有对应英文:\n' + log_template + '\n' + k + '\n--------------')
            for i, param in enumerate(params_template):
                repl = param.strip(']') + ':param{}]'.format(i)
                # 转义正则表达式中的特殊字符
                param_escape = re.escape(param)
                log_template = re.sub(param_escape, repl, log_template, count=1)

        # # if re.match('-.*?;', '', log_template):
        # match = re.match('-.*?;', log_template, re.S)
        # if match:
        #     i = match.span()[1]
        #     # print('xxxxx')
        #     log_template = log_template[i:].strip()

        v['log_template_with_field'] = log_template.strip()

    return logs_cn


def main():

    result = merge_cn_en(cn_path='files/result_cn.xls', en_path='files/result_en.xls')

    # split_log_pattern(result)

    # count = 0
    # for k, v in result.items():
    #     if len(v) != 6:
    #         count += 1
    #         print(str(len(v)) + '    ' + k + '\n-------------------')
    #
    # print(count)

    # 创建一个Workbook对象，相当于创建了一个Excel文件
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)

    # 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
    sheet = book.add_sheet('test01', cell_overwrite_ok=True)
    # 其中的test是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

    for i, (k, v) in enumerate(result.items()):
        sheet.write(i, 0, k)
        sheet.write(i, 1, v['log_template'])
        sheet.write(i, 2, v['log_desc'])
        sheet.write(i, 3, v['variable_fields'])
        sheet.write(i, 4, v['log_explanation'])
        sheet.write(i, 5, v['log_recommended_action'])
        sheet.write(i, 6, v['log_template_with_field'])
        # if len(v) == 6:
        #     sheet.write(i, 6, v[5])

    book.save("files/result_cn_with_en_variables.xls")


if __name__ == '__main__':
    main()


