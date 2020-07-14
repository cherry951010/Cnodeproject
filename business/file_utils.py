"""
封装处理不同解析文件的方法
"""
import json
def parse_from_json(filepath):
    data = json.load(open(filepath,mode='r',encoding='utf8'))
    testdata = data['test_create_topics']
    return testdata