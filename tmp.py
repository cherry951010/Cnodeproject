import  json

#json 编码
test = ['foo',{'bar':('baz',None,1.0,2)}]
data = json.dumps(test)
print(data,type(data))
#json 解码
test_str = '{"usernam":"xiaomin"}'
data = json.loads(test_str)
print(data,type(data))
#加载json文件转换Python格式load
data = json.load(open('data/topics.json',mode='r',encoding='utf8'))
print(data,type(data))
#写入文件
data = ['foo',{'bar':('baz',None,1.0,2)}]
json.dump(data,open('data/tmp.json',mode='w',encoding='utf8'))



