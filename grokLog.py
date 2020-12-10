# coding:utf-8
from pygrok import Grok
import json
from pattern_logs import get_pattern_logs
import time
from kafka import KafkaConsumer
from kafka import KafkaProducer

def parse_base(syslog):
    pattern = "<%{NUMBER:pri:int}>(?<logTime>(%{MONTH} +%{MONTHDAY} %{TIME}( %{YEAR})?|%{MONTH} +%{MONTHDAY} %{YEAR} %{TIME})) %{DATA:loghostname} %%%{NUMBER}%{DATA:module}/%{NUMBER:severity:int}/%{DATA:logTypeDesc}:(( -%{DATA:location};)?|(s)?) +%{GREEDYDATA:desc}"
    grok = Grok(pattern)
    raw_log = syslog["message"]
    parsed_log = grok.match(raw_log)
    if parsed_log:
        # return parsed_log
        syslog.update(parsed_log)


def parse_multi_patterns(patterns_arr, text):
    # 同一种日志，多种表现形式
    for p in patterns_arr:
        parsed_text = Grok(p).match(text)
        if parsed_text is not None:
            return parsed_text

    # return None


def parse_multi_types(pattern_logs, text):
    # 一个描述符对应多种类型日志
    for pattern_log in pattern_logs:
        patterns = pattern_log["patterns"]
        parsed_event = parse_multi_patterns(patterns, text)
        if parsed_event is not None:
            for k, v in pattern_log.items():
                if k != "patterns":
                    parsed_event[k] = v
            return parsed_event
        else:
            pass


def parse_log_event(event_json):

    event = json.loads(event_json)

    module = event['module']
    log_type_desc = event['logTypeDesc']
    desc = event['desc']

    # parsed_event = None
    pattern_logs = get_pattern_logs(module, log_type_desc)

    if pattern_logs:
        parsed_event = parse_multi_types(pattern_logs, desc)

        if parsed_event:
            event.update(parsed_event)

    # event_json = json.dumps(event, ensure_ascii=False)
    return event


def test_parse_base():
    # raw_log = "<174>Jul  7 01:33:51 2020 67-215 %%10SHELL/6/SHELL_CMD: -Line=aux0-IPAddr=**-User=**; Command is quit."
    syslog = {
        "timestamp": "2020-07-15T15:21:19+08:00",
        "message": "<174>Jul 15 15:21:19 2020 67-215 %%10SSHS/6/SSHS_AUTH_SUCCESS: SSH user admin from 10.99.216.68 port 50958 passed password authentication.",
        "host": "192.168.67.215"}
    parse_base(syslog)
    syslog_json = json.dumps(syslog)
    print(syslog_json)


def test_parse_log_event():
    # raw_log = "<174>Jul  7 01:33:51 2020 67-215 %%10ACL/4/ACL_ACCELERATE_NO_RES: Failed to accelerate IPv6 ACL 2001. The resources are insufficient."
    # end = time.time()
    # print("Start cost {} s".format(end-start))
    while True:
        try:
            raw_log = input("Please input log message: ")
            syslog = {
                "timestamp": "2020-07-15T15:21:19+08:00",
                "message": raw_log,
                "host": "192.168.67.215"}
            tic = time.time()
            print("raw syslog : \n{}".format(syslog))
            parse_base(syslog)
            syslog_json = json.dumps(syslog)
            # event_json = json.dumps(event)

            event_json = parse_log_event(syslog_json)
            # event_json = event_json.encode('utf-8')
            # event_json = json.dumps(event)
            print("Parsed result: \n{}".format(event_json))
            toc = time.time()

            print("Cost {} s".format(toc-tic))
        except KeyError as e:
            print(e)


def parse_kafka(topic_source='rsyslog', topic_sink='security'):
    consumer = KafkaConsumer(topic_source, bootstrap_servers=['192.168.179.232:30091'], value_deserializer=bytes.decode)
    producer = KafkaProducer(bootstrap_servers=['192.168.179.232:30091'], )
    end = time.time()
    print("Start cost {} s".format(end-start))
    for msg in consumer:
        syslog = msg.value
        tic = time.time()
        print("raw syslog : \n{}".format(syslog))
        syslog = json.loads(syslog)
        parse_base(syslog)
        syslog_json = json.dumps(syslog)
        # event_json = json.dumps(event)

        event = parse_log_event(syslog_json)
        # event_json = event_json.encode('utf-8')
        # event_json = json.dumps(event)
        event_json = json.dumps(event, ensure_ascii=False)
        print("Parsed result: \n{}".format(event_json))
        toc = time.time()

        print("Cost {} s".format(toc - tic))

        future = producer.send(topic_sink, value=event, partition=0)
        result = future.get(timeout=10)
        print(result)
        print("-----------------")


if __name__ == "__main__":

    start = time.time()

    # test_parse_log_event()
    # test_parse_base()
    parse_kafka(topic_source="rsyslog", topic_sink="security")



