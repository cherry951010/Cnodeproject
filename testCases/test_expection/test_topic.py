"""
测试 发布话题的异常场景

"""
import  requests
import  pytest
defaulturl = 'http://49.233.108.117:3000/api/v1'
accesstoken = 'ebb04940-7910-4f74-a175-fe5dd01cb0f9'
testdata = [
    ({'accesstoken':'1','title':'','tab':'','content':''},401,'错误的accessToken'),
    ({'accesstoken':accesstoken,'title':'1111111','tab':'','content':''},400,'必须选择一个版块'),
    ({'accesstoken':accesstoken,'title':'','tab':'','content':''},400,'标题不能为空'),
    ({'accesstoken':accesstoken,'title':'1','tab':'','content':''},400,'标题字数太多或太少'),
    ({'accesstoken':accesstoken,'title':'hellowoed','tab':'ask','content':''},400,'内容不可为空')
]


@pytest.mark.parametrize('topic_data,code,errormsg',testdata)

def test_create_topic(topic_data,code,errormsg):
    url = defaulturl + '/topics'
    res = requests.post(url=url,data=topic_data)
    jsondata = res.json()
    assert jsondata['success'] == False
    print(res.json(),code,errormsg)
    assert res.status_code == code
    assert res.json()['error_msg'] == errormsg
    return jsondata
    pass





