"""
测试 发布话题的异常场景

"""
import  requests
import  pytest
defaulturl = 'http://49.233.108.117:3000/api/v1'
testdata = [
    {'accesstoken':'1','title':'','tab':'','content':''},
    {'accesstoken':'2','title':'1111111','tab':'','content':''},
    {'accesstoken':'3','title':'','tab':'','content':''},
    {'accesstoken':'4','title':'','tab':'','content':''},
    {'accesstoken':'5','title':'','tab':'','content':''}
]
'/topics'
@pytest.mark.parametrize('topic_data',testdata)
def test_create_topic(topic_data):
    # print(topic_data)

    url =defaulturl + '/topics'
    res = requests.post(url=url,data=testdata)
    assert res.status_code == 401
