
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




raw_rule = """

grok {{
	match => {{
		"message" => "<%{{NUMBER:pri:int}}>(?<logTime>(%{{MONTH}} +%{{MONTHDAY}} %{{TIME}}( %{{YEAR}})?|%{{MONTH}} +%{{MONTHDAY}} %{{YEAR}} %{{TIME}})) %{{DATA:loghostname}} %%%{{NUMBER}}%{{DATA:module}}/%{{NUMBER:severity:int}}/%{{DATA:logTypeDesc}}:(( -%{{DATA:location}};)?|(s)?) +%{{GREEDYDATA:desc}}"
	}}
}}

date {{
	match => [ "logTime", "MMM dd HH:mm:ss YYYY",  "MMM dd YYYY HH:mm:ss", "MMM dd HH:mm:ss", "YYYY/MM/dd HH:mm:ss", "MMM  d HH:mm:ss YYYY", "MMM  d YYYY HH:mm:ss", "MMM dd HH:mm:ss", "ISO8601" ]
	target => "logTime"
}}

kv {{
	source => "location"
	field_split => "-"
	value_split => "="
	remove_field => ["location"]
}}

uuid {{
	target => "ldp_uuid"
	overwrite => true
}}

mutate {{
	rename => {{
		"host" => "ldp_host_ip"
	}}
	remove_field => ["timestamp"]
	add_field => {{
		"ldp_timestamp" => "%{{@timestamp}}"
	}}
}}
#登录失败时
if[module]== "LOGIN"{{
	if[logTypeDesc]== "LOGIN_FAILED" {{
		grok {{
			match => {{"desc" => "%{{DATA:user}} failed to log in from %{{DATA:userIp}}."}}
			add_field => {{
				"action" => "login"
				"loginStatus" => "failed"
			}}
		}}
	}}
}} else if[module]== "SHELL" {{
	grok {{
		match => {{
			"desc" => "((%{{GREEDYDATA:params}};)?)((s)?)%{{GREEDYDATA:msg}}"
		}}
	}}
	new_kv {{
		source => "params"
		field_split => "-"
		value_split => "="
		omit_empty_fields => false
		trim_value_split => false
		include_brackets => false
		remove_field => ["params"]
	}}
	if[logTypeDesc]== "SHELL_CMD" or [logTypeDesc]== "SHELL_CMD(l)"{{
		grok {{
			match => {{
				"msg" => "Command is %{{GREEDYDATA:command}}"
			}}
		}}
		mutate {{
			copy => {{ "command" => "temp_command" }}
		}}
		mutate {{
			lowercase => [ "temp_command" ]
		}}
		if [temp_command]== "exit" or [temp_command]== "quit" {{
			mutate {{
				add_field => {{
					"action" => "logout"
					"logoutStatus" => "success"
					}}
			}}
		}}
		mutate {{
			remove_field => ["temp_command"]
		}}
	}}else if[logTypeDesc]== "SHELL_CMD_CONFIRM"{{
		grok {{
			match => {{
				"msg" => "Confirm option of command %{{DATA:command}} is %{{DATA:result}}.$"
			}}
		}}
	}}else if[logTypeDesc]== "SHELL_CMD_EXECUTEFAIL"{{
		grok {{
			match => {{
				"msg" => "Command %{{DATA:command}} in view %{{DATA:view}} failed to be executed."
			}}
		}}
	}}else if[logTypeDesc]== "SHELL_CMD_MATCHFAIL"{{
		grok {{
			match => {{
				"msg" => "Command %{{DATA:command}} in view %{{DATA:view}} failed to be matched."
			}}
		}}
	}}else if[logTypeDesc]== "SHELL_LOGIN" or [logTypeDesc]== "SHELL_LOGIN(l)"{{
		grok {{
			match => {{
				"msg" => "%{{DATA:user}} logged in from %{{DATA:userIp}}.$"
			}}
			add_field => {{
				"action" => "login"
				"loginStatus" => "success"
				}}
		}}
	}}else if[logTypeDesc]== "SHELL_LOGOUT" or [logTypeDesc]== "SHELL_LOGOUT(l)" {{
		grok {{
			match => {{
				"msg" => "%{{DATA:user}} logged out from %{{DATA:userIp}}.$"
			}}
			add_field => {{
				"action" => "logout"
				"logoutStatus" => "success"
				}}
		}}
	}}else if[logTypeDesc]== "LOGIN(t)" or [logTypeDesc]== "LOGOUT(t)" {{
		grok {{
			match => {{
				"msg" => ".:%{{DATA:user}} %{{DATA:action}} from %{{GREEDYDATA:userIp}}"
			}}
		}}
	}}else if[logTypeDesc]== "LOGIN_FAILED"  {{
		grok {{
			match => {{"msg" => "%{{DATA:user}} failed to log in from %{{DATA:userIp}}."}}
			add_field => {{
				"action" => "login"
				"loginStatus" => "failed"
			}}
		}}
	}}
}}{0} else {{
	mutate {{
		add_field => {{ "msg" => "%{{desc}}"}}
	}}
	if[logTypeDesc]== "INTERFACE UPDOWN(t)" {{
		grok {{
			match => {{
				"msg" => ".: Interface %{{NUMBER:interface}} is %{{GREEDYDATA:interfaceStatus}}, ifAdminStatus is %{{NUMBER:ifAdminStatus:int}}, ifOperStatus is %{{NUMBER:ifOperStatus:int}}"
			}}
		}}
	}}else if[logTypeDesc]== "LINK_UPDOWN" {{
		grok {{
			match => {{
				"msg" => "Line protocol on the interface %{{GREEDYDATA:interface}} is %{{GREEDYDATA:interfaceStatus}}."
			}}
		}}
	}}else if[logTypeDesc]== "LINK_UPDOWN(l)" or [logTypeDesc]== "PHY_UPDOWN" {{
		grok {{
			match => {{
				"msg" => "%{{GREEDYDATA:interface}} link status is %{{GREEDYDATA:interfaceStatus}}."
			}}
		}}
	}}else if[logTypeDesc]== "SSHS_AUTH_EXCEED_RETRY_TIMES"  {{
		grok {{
			match => {{
				 "msg" => "SSH user %{{DATA:user}} \\(IP: %{{DATA:userIp}}\\) failed to log in, because the number of authentication attempts exceeded the upper limit.[\\u0000]?"
			}}
		}}
	}} else if[logTypeDesc]== "SSHS_CONNECT"  {{

		grok {{
				 match => {{
						   "msg" => "SSH user %{{DATA:user}} \\(IP: %{{DATA:userIp}}\\) connected to the server successfully.[\\u0000]?"
				 }}
		}}
	}} else if[logTypeDesc]== "SSHS_DISCONNECT"  {{
		grok {{
				 match => {{
						   "msg" => "SSH user %{{DATA:user}} \\(IP: %{{DATA:userIp}}\\) disconnected from the server.[\\u0000]?"
				 }}
		}}
	}} else if[logTypeDesc]== "SSHS_LOG"  {{
		grok {{
				 match => {{
						   "msg" => "Authentication failed for %{{DATA:user}} from %{{DATA:userIp}} port %{{DATA:userPort}} ssh2.[\\u0000]?"
				 }}
		}}
	}}
}}

mutate {{
	lowercase => [ "interfaceStatus" ]
}}
if [severity] == 0 {{
	mutate {{
		add_field => {{ "severityLevel" => "危急" }}
	}}
}} else if [severity] == 1 {{
	mutate {{
		add_field => {{ "severityLevel" => "报警" }}
	}}
}} else if [severity] == 2 {{
	mutate {{
		add_field => {{ "severityLevel" => "严重" }}
	}}
}} else if [severity] == 3 {{
	mutate {{
		add_field => {{ "severityLevel" => "错误" }}
	}}
}} else if [severity] == 4 {{
	mutate {{
		add_field => {{ "severityLevel" => "告警" }}
	}}
}} else if [severity] == 5 {{
	mutate {{
		add_field => {{ "severityLevel" => "提示" }}
	}}
}} else if [severity] == 6 {{
	mutate {{
		add_field => {{ "severityLevel" => "信息" }}
	}}
}} else if [severity] == 7 {{
	mutate {{
		add_field => {{ "severityLevel" => "调试" }}
	}}
}} else {{
	mutate {{
		add_field => {{ "severityLevel" => "未知" }}
	}}
}}

mutate {{
	remove_field => ["desc"]
}}

ruby {{
	code => "
		event.to_hash.each do |k, v|
			if ''.eql?(v)
				event.remove(k)
			end
		end
	"
}}

if "_grokparsefailure" in [tags] or "_dateparsefailure" in [tags] or "_geoip_lookup_failure" in [tags] or "_jsonparsefailure" in [tags] or "_rubyexception" in [tags] {{
	mutate {{
		add_field => {{ "parse_success" => false }}
	}}
}} else {{
	mutate {{
		add_field => {{ "parse_success" => true }}
	}}
	mutate {{
		remove_field => ["message"]
	}}
}}

if "_grokparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "grok解析失败" }}
	}}
}}

if "_dateparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "date解析失败" }}
	}}
}}

if "_geoip_lookup_failure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "ip解析失败" }}
	}}
}}

if "_jsonparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "json解析失败" }}
	}}
}}

if "_rubyexception" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "ruby解析失败" }}
	}}
}}

"""


rule_stable = """
grok {{
	match => {{
		"message" => "<%{{NUMBER:pri:int}}>(?<logTime>(%{{MONTH}} +%{{MONTHDAY}} %{{TIME}}( %{{YEAR}})?|%{{MONTH}} +%{{MONTHDAY}} %{{YEAR}} %{{TIME}})) %{{DATA:loghostname}} %%%{{NUMBER}}%{{DATA:module}}/%{{NUMBER:severity:int}}/%{{DATA:logTypeDesc}}:(( -%{{DATA:location}};)?|(s)?) +%{{GREEDYDATA:desc}}"
	}}
}}

date {{
	match => [ "logTime", "MMM dd HH:mm:ss YYYY",  "MMM dd YYYY HH:mm:ss", "MMM dd HH:mm:ss", "YYYY/MM/dd HH:mm:ss", "MMM  d HH:mm:ss YYYY", "MMM  d YYYY HH:mm:ss", "MMM dd HH:mm:ss", "ISO8601" ]
	target => "logTime"
}}

kv {{
	source => "location"
	field_split => "-"
	value_split => "="
	remove_field => ["location"]
}}

uuid {{
	target => "ldp_uuid"
	overwrite => true
}}

mutate {{
	rename => {{
		"host" => "ldp_host_ip"
	}}
	remove_field => ["timestamp"]
	add_field => {{
		"ldp_timestamp" => "%{{@timestamp}}"
	}}
}}

{}


if [severity] == 0 {{
	mutate {{
		add_field => {{ "severityLevel" => "危急" }}
	}}
}} else if [severity] == 1 {{
	mutate {{
		add_field => {{ "severityLevel" => "报警" }}
	}}
}} else if [severity] == 2 {{
	mutate {{
		add_field => {{ "severityLevel" => "严重" }}
	}}
}} else if [severity] == 3 {{
	mutate {{
		add_field => {{ "severityLevel" => "错误" }}
	}}
}} else if [severity] == 4 {{
	mutate {{
		add_field => {{ "severityLevel" => "告警" }}
	}}
}} else if [severity] == 5 {{
	mutate {{
		add_field => {{ "severityLevel" => "提示" }}
	}}
}} else if [severity] == 6 {{
	mutate {{
		add_field => {{ "severityLevel" => "信息" }}
	}}
}} else if [severity] == 7 {{
	mutate {{
		add_field => {{ "severityLevel" => "调试" }}
	}}
}} else {{
	mutate {{
		add_field => {{ "severityLevel" => "未知" }}
	}}
}}

ruby {{
	code => "
		event.to_hash.each do |k, v|
			if ''.eql?(v)
				event.remove(k)
			end
		end
	"
}}

if "_grokparsefailure" in [tags] or "_dateparsefailure" in [tags] or "_geoip_lookup_failure" in [tags] or "_jsonparsefailure" in [tags] or "_rubyexception" in [tags] {{
	mutate {{
		add_field => {{ "parse_success" => false }}
	}}
}} else {{
	mutate {{
		add_field => {{ "parse_success" => true }}
	}}
	mutate {{
		remove_field => ["message"]
	}}
}}

if "_grokparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "grok解析失败" }}
	}}
}}

if "_dateparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "date解析失败" }}
	}}
}}

if "_geoip_lookup_failure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "ip解析失败" }}
	}}
}}

if "_jsonparsefailure" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "json解析失败" }}
	}}
}}

if "_rubyexception" in [tags] {{
	mutate {{
		add_field => {{ "failure_reason" => "ruby解析失败" }}
	}}
}}

"""




def generate_rule(logs):

    # content = ''

    module_format = '''
{0}[module]== "{1}" {{
    {2}
}}
'''

    logTypeDesc_format = '''
    {0}[logTypeDesc]== "{1}" {{
        {2}
    }}
'''

    dissect_format_single = '''
		dissect {{
			mapping => {{
				"desc" => {0}
			}}

            add_field => {{ "log_explanation" => "{1}" }}
            add_field => {{ "log_recommended_action" => "{2}" }}
		}}
'''

    grok_format_single = '''
    		grok {{
    			match => {{
    				"desc" => {0}
    			}}

                add_field => {{ "log_explanation" => "{1}" }}
                add_field => {{ "log_recommended_action" => "{2}" }}
    		}}
    '''

    dissect_format_multi = '''
        	dissect {{
    			mapping => {{
    			    "desc" => {0}
    			}}
                add_field => {{ "log_explanation" => "{1}" }}
                add_field => {{ "log_recommended_action" => "{2}" }}
                add_field => {{ "type_%{{logTypeDesc}}" => "type{3}"  }}
    		}} 
    '''

    grok_format_multi = '''
        	grok {{
    			match => {{
    			    "desc" => {0}
    			}}
                add_field => {{ "log_explanation" => "{1}" }}
                add_field => {{ "log_recommended_action" => "{2}" }}
                add_field => {{ "type_%{{logTypeDesc}}" => "type{3}"  }}
    		}} 
    '''

    rules = ''

    for index_m, (k0, v0) in enumerate(logs.items()):

        module = k0
        desc_dict = v0  # 二层dictionary

        # if module.strip() == "IPFW":
        #     print(module)

        desc_text = ''
        for j, (k1, v1) in enumerate(desc_dict.items()):
            desc = k1

            # v1为一个二层list
            if len(v1) > 1:
                # 一个描述符对应多种类型日志
                grok_text = ''

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
                    if len(templates) > 1:
                        msgs = []
                        for template in templates:
                            msg = template2msg_grok(template)
                            if msg:
                                msgs.append(msg)
                        msgs = json.dumps(msgs)
                        rule_grok = grok_format_multi.format(msgs, log_explanation, log_recommended_action, i)
                    else:
                        template = templates[0]
                        msg = template2msg_dissect(template)

                        if re.search('%{.*}', msg):
                            msg = '"' + msg + '"'
                            rule_grok = dissect_format_multi.format(msg, log_explanation, log_recommended_action, i)
                        else:
                            msg = '"' + msg + '"'
                            rule_grok = grok_format_multi.format(msg, log_explanation, log_recommended_action, i)

                # rule_grok = rule_grok.replace('\'', '\"')

                    grok_text += rule_grok
            else:
                log_detail = v1[0]
                log_template_with_field = log_detail[-1]
                log_recommended_action = log_detail[-2]
                log_explanation = log_detail[-3]

                log_template_with_field = re.sub('\(', '\\(', log_template_with_field)
                log_template_with_field = re.sub('\)', '\\)', log_template_with_field)

                log_recommended_action = re.sub('"', '\\"', log_recommended_action)
                log_explanation = re.sub('"', '\\"', log_explanation)

                templates = re.split("形式.*[：:]|或", log_template_with_field.strip())
                if len(templates) > 1:
                    msgs = []
                    for template in templates:
                        msg = template2msg_grok(template)
                        if msg:
                            msgs.append(msg)

                    msgs = json.dumps(msgs)
                    rule_grok = grok_format_single.format(msgs, log_explanation, log_recommended_action)
                else:
                    template = templates[0]
                    msg = template2msg_dissect(template)

                    if re.search('%{.*}', msg):
                        msg = '"' + msg + '"'
                        rule_grok = dissect_format_single.format(msg, log_explanation, log_recommended_action)

                    else:
                        msg = '"' + msg + '"'
                        rule_grok = grok_format_single.format(msg, log_explanation, log_recommended_action)

                # rule_grok = rule_grok.replace('\'', '\"')

                grok_text = rule_grok

            if j == 0:
                rule_log_type_desc = logTypeDesc_format.format('if', desc, grok_text)
            else:
                rule_log_type_desc = logTypeDesc_format.format('else if', desc, grok_text)

            desc_text += rule_log_type_desc

        if index_m == 0:
            module_rule = module_format.format('if', module, desc_text)
        else:
            module_rule = module_format.format('else if', module, desc_text)

        rules += module_rule

    # new_rules = raw_rule.format(rules)
    new_rules = rule_stable.format(rules)

    return new_rules

"""
        rule_desc = ''
        for i, e in enumerate(desc_templates):
            if i == 0:
                s0 = 'if'
            else:
                s0 = 'else if'

            s1 = e[0]

            '''
            这里是为了处理类似模板：（NAT/4/NAT_SERVICE_CARD_RECOVER_FAILURE）
            形式一：

            Failed to recover the configuration of binding the service card on slot [UINT16] to interface [STRING], because [STRING].

            形式二：

            Failed to recover the configuration of binding the service card on chassis [UINT16] slot [UINT16] to interface [STRING], because [STRING].
            '''
            templates = re.split("形式.*[：:]", e[1].strip())

            templates_clean = []
            for t in templates:
                if t:
                    templates_clean.append(t.strip())

            if len(templates_clean) > 1:
                s2_list = []
                for t in templates_clean:
                    s2_list.append(template2rule(t))

                s2 = str(s2_list)

            else:
                s2 = template2rule(templates_clean[0])

            rule_desc_tmp = rule_format.format(s0, s1, s2)
            rule_desc += rule_desc_tmp

        rule_module_tmp = '''
        else if [module] == "{0}"{{
            mutate {{
            add_field => {{ "msg" => "%{{desc}}"}}
            }}
            {1}
        }}
        '''.format(module, rule_desc)

        rules += rule_module_tmp
"""


def template2msg_dissect(log_template):
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
        # data_type = data_type.strip('[')
        field = field.strip(']')
        # data_type_logstash = repl_map[data_type]

        # param_repl = re.sub(data_type, data_type_logstash, param)

        # if data_type_logstash is "NUMBER":
        #     param_repl = re.sub('\[', '%{', param_repl)
        #     param_repl = re.sub('\]', ':int}', param_repl)
        # elif re.match('\(.*\)', data_type_logstash):
        #     param_repl = param_repl.strip('[]')
        # else:
        #     param_repl = re.sub('\[', '%{', param_repl)
        #     param_repl = re.sub('\]', '}', param_repl)

        # 转义正则表达式中的特殊字符
        param_escape = re.escape(param)
        content = re.sub(param_escape, "%{" + field + "}", content, count=1)
        # data_type_logstash = repl_map[param]
        # if data_type_logstash is "NUMBER":
        #     repl = '%{{{0}:param{1}:int}}'.format(data_type_logstash, i)
        # else:
        #     repl = '%{{{0}:param{1}}}'.format(data_type_logstash, i)

    # dissect不需要转义
    content = re.sub('\\(', '\(', content)
    content = re.sub('\\)', '\)', content)

    return content


def template2msg_grok(log_template):
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
        # data_type_logstash = repl_map[param]
        # if data_type_logstash is "NUMBER":
        #     repl = '%{{{0}:param{1}:int}}'.format(data_type_logstash, i)
        # else:
        #     repl = '%{{{0}:param{1}}}'.format(data_type_logstash, i)

    return content


def template2msg_test():
    log_template = '-NeighborName=[STRING:ANCP_neighbor_name]-State=[STRING:Neighbor_state]-MessageType=[STRING:Message_type]; The [STRING:Field] value [STRING:Wrong_value_of_the_field] is wrong, and the value [STRING:Expected_value_of_the_field] is expected.'
    content = template2msg_dissect(log_template)
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


    #     print(log_desc)
    #     if log_desc:
    #         module, severity, desc = log_desc.split(r"/")
    #
    #         if module not in logs:
    #             logs[module] = {desc: [log_template]}
    #         elif desc not in logs[module]:
    #             logs[module][desc] = [log_template]
    #         else:
    #             print("PROBLEM!!!!!!!!!!!")
    #             print(module, desc, log_template)
    #             logs[module][desc].append(log_template)
    #
    # rule = generate_rule(logs)
    #
    # with open(rule_output, "w") as f_rule:
    #     f_rule.write(rule)


if __name__ == "__main__":
    main('result_cn_with_en_variables.xls', 'rule_dissect.txt')
    # template2msg_test()





