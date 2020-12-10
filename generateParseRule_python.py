
import re
import xlrd
import json

repl_map = {'TIME': 'TIME', 'USHOT': 'NUMBER', 'USHORT': 'NUMBER', 'IPADDR': 'IP',
            'NUMBER': 'NUMBER', 'DATE': '(?<LOG_DATE>%{MONTH} +%{MONTHDAY})', 'microsegment-id': 'NUMBER',
            'UNIT16': 'NUMBER', 'IPV6ADDR': 'IPV6', 'ULONG': 'NUMBER', 'STRINT':'DATA',
            'UCHAR': 'NUMBER', 'UNIT32': 'NUMBER',  'CHAR': 'DATA', 'UNIT': 'NUMBER',
            'string': 'DATA', 'UINT16': 'NUMBER', 'STRIING': 'DATA', 'DOUBLE': 'DATA',
            'STRING': 'DATA', 'MAC': 'MAC', 'INT32': 'NUMBER', 'UINT8': 'NUMBER',
            'UINT64': 'NUMBER', '%s': 'DATA', 'UINT32': 'NUMBER', 'UINT': 'NUMBER',
            'INTEGER': 'NUMBER', 'HEX': 'DATA'}


def generate_rule(logs):

    # content = ''

    module_format = '''
    {0} module == "{1}":
        {2}
'''

    logTypeDesc_format = '''
        {0} log_type_desc == "{1}":
            pattern_logs = {2}
'''

#     grok_format_single = '''
# 		grok {{
# 			match => {{
# 				"desc" => {0}
# 			}}
#
#             add_field => {{ "log_explanation" => "{1}" }}
#             add_field => {{ "log_recommended_action" => "{2}" }}
# 		}}
# '''
#
#     grok_format_multi = '''
#         	grok {{
#     			match => {{
#     			    "desc" => {0}
#     			}}
#                 add_field => {{ "log_explanation" => "{1}" }}
#                 add_field => {{ "log_recommended_action" => "{2}" }}
#                 add_field => {{ "type_%{{logTypeDesc}}" => "type{3}"  }}
#     		}}
#     '''

    rules = ''

    # gram_pattern = "pattern_logs = {0}"

    for index_m, (k0, v0) in enumerate(logs.items()):

        module = k0
        desc_dict = v0  # 二层dictionary

        # if module.strip() == "IPFW":
        #     print(module)

        desc_text = ''
        for j, (k1, v1) in enumerate(desc_dict.items()):
            desc = k1
            pattern_logs = []

            for i, log_detail in enumerate(v1):
            # log_detail: [log_example, log_template, log_desc, variable_fields, log_explanation, log_recommended_action, log_template_with_field]
                log_template_with_field = log_detail[-1]
                log_recommended_action = log_detail[-2]
                log_explanation = log_detail[-3]

                log_template_with_field = re.sub('\(', '\\(', log_template_with_field)
                log_template_with_field = re.sub('\)', '\\)', log_template_with_field)

                log_recommended_action = re.sub('"', '\\"', log_recommended_action)
                log_explanation = re.sub('"', '\\"', log_explanation)

                # 一种log有多种表现形式
                templates = re.split("形式.*[：:]|或", log_template_with_field.strip())

                msgs = []
                for template in templates:
                    msg = template2msg(template)
                    if msg:
                        msgs.append(msg)

                pattern_log = {
                    "patterns": msgs,
                    "log_explanation": log_explanation,
                    "log_recommended_action": log_recommended_action
                }

                pattern_logs.append(pattern_log)

            if j == 0:
                rule_log_type_desc = logTypeDesc_format.format('if', desc, pattern_logs)
            else:
                rule_log_type_desc = logTypeDesc_format.format('elif', desc, pattern_logs)

            desc_text += rule_log_type_desc

        if index_m == 0:
            module_rule = module_format.format('if', module, desc_text)
        else:
            module_rule = module_format.format('elif', module, desc_text)

        rules += module_rule

    # new_rules = raw_rule.format(rules)
    # gram_pattern.format(pattern_logs)
    # new_rules = rule_stable.format(rules)

    return rules


def template2msg(log_template):
    """
    :param log_template: press上爬取的日志模板
    eg. -NeighborName=[STRING:ANCP_neighbor_name]-State=[STRING:Neighbor_state]-MessageType=[STRING:Message_type]; The [STRING:Field] value [STRING:Wrong_value_of_the_field] is wrong, and the value [STRING:Expected_value_of_the_field] is expected.
    :return: logstash解析的规则
    """

    # 去除location部分的信息
    # re.S即re.DOTALL,让 '.' 特殊字符匹配任何字符，包括换行符，考虑到有的log不止一行
    match = re.match('-.*?;', log_template, re.S)

    if match:
        span = match.span()
        content = log_template[span[1]:].strip()
    else:
        content = log_template.strip()

    params_in_template = re.findall('\[[^\[]*?\]', content)

    for i, param in enumerate(params_in_template):

        # param [STRING:ANCP_neighbor_name]
        data_type, field = param.split(':')
        data_type = data_type.strip('[')
        # field = field.strip(']')
        data_type_logstash = repl_map[data_type]

        param_repl = re.sub(data_type, data_type_logstash, param)

        if data_type_logstash is "NUMBER":
            param_repl = re.sub('\[', '%{', param_repl)
            param_repl = re.sub('\]', ':int}', param_repl)
        elif re.match('\(.*\)', data_type_logstash):
            param_repl = param_repl.strip('[]')
        else:
            param_repl = re.sub('\[', '%{', param_repl)
            param_repl = re.sub('\]', '}', param_repl)

        # 转义正则表达式中的特殊字符
        param_escape = re.escape(param)
        content = re.sub(param_escape, param_repl, content, count=1)

    return content


def template2msg_test():
    log_template = '-NeighborName=[STRING:ANCP_neighbor_name]-State=[STRING:Neighbor_state]-MessageType=[STRING:Message_type]; The [STRING:Field] value [STRING:Wrong_value_of_the_field] is wrong, and the value [STRING:Expected_value_of_the_field] is expected.'
    content = template2msg(log_template)
    print(content)


def main(log_file, rule_output):
    logs = {}
    # 操作excel
    excel = xlrd.open_workbook(log_file)
    # excel.sheet_names()  # 获取excel里的工作表sheet名称数组
    sheet = excel.sheet_by_index(0)  # 根据下标获取对应的sheet表

    n_rows = sheet.nrows  # 获取总共的行数
    for row in range(1, n_rows):
        row_list = sheet.row_values(row)    # 每一行的数据在row_list 数组里

        if len(row_list) == 7:
            log_example, log_template, log_desc, variable_fields, log_explanation, log_recommended_action, log_template_with_field = row_list
        else:
            print("第{}行异常".format(row))
            continue

        print(log_desc)

        # press的格式有错误
        if log_desc == "QOS/4QOS_POLICY_APPLYVLAN_CBFAIL":
            log_desc = "QOS/4/QOS_POLICY_APPLYVLAN_CBFAIL"
            log_example = re.sub("QOS/4QOS_POLICY_APPLYVLAN_CBFAIL", "QOS/4/QOS_POLICY_APPLYVLAN_CBFAIL", log_example)
        module, severity, desc = log_desc.split('/')

        if module not in logs:
            logs[module] = {}
            logs[module][desc] = [[log_template, log_desc, variable_fields, log_example,
                                   log_explanation, log_recommended_action, log_template_with_field]]
        elif desc not in logs[module]:
            logs[module][desc] = [[log_template, log_desc, variable_fields, log_example,
                                   log_explanation, log_recommended_action, log_template_with_field]]
        else:
            logs[module][desc].append([log_template, log_desc, variable_fields, log_example,
                                       log_explanation, log_recommended_action, log_template_with_field])

    rule = generate_rule(logs)

    with open(rule_output, 'w', encoding='utf-8') as f:
        f.writelines(rule)


if __name__ == "__main__":
    main('files/result_cn_with_en_variables.xls', 'files/rule_python.py')
    # template2msg_test()





