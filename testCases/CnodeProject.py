from business.common import Create_topic, Get_token, Get_topic_detail, Get_username, Other_token, Get_reply_id, \
Get_verfily_token, Get_hasnot_number, Get_allmessageNum, Get_markPartMessage
from business.logger import logger

accesstoken = 'ebb04940-7910-4f74-a175-fe5dd01cb0f9'
other_token = '81ccd1d9-be88-43b6-b288-b17293300f32'
defaulturl = 'http://49.233.108.117:3000/api/v1'
'''
主要测试Cnode社区的的话题相关的功能
'''
import requests
# def test_topic_page(method,url,page,type,limit):
#     """
#     测试主题首页功能
#     :param page:
#     :param type:
#     :param limit:
#     :return:
#     """
#     url1 = url
#     parmas = {'page': page,
#               'type': type,
#               'limit': limit
#               }
#     request = requests.request(method=method,url=url1,params=parmas).json()
#     return request
#
# def test_New_Creat_topic(url,title,tab,content):
#     """
#     创建主题
#     :return:
#     """
#     url1 = defaulturl+url
#     data = {
#             'accesstoken':accesstoken,
#             'title':title,
#             'tab':tab,
#             'content':content
#     }
#     res = requests.post(url=url1,data=data).json()
#     return res

def test_View_topic():
    """
    id主题详情页
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    topic_id = Create_topic(data)

    url = defaulturl +'/topic/' + topic_id
    logger.debug(f'发送请求：{url}')
    res1 = requests.get(url)
    assert  res1.status_code == 200
    jsondata = res1.json()
    assert data['title'] == jsondata['data']['title']
    assert data['tab'] == jsondata['data']['tab']
    assert data['content'] in jsondata['data']['content']

    # return jsondata
# print(test_View_topic())

def test_editor_topic():
    """
    更新帖子
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    topic_id = Create_topic(data)

    url=defaulturl+'/topics/update'
    logger.debug(f'发送请求：{url}')

    update_data = {
        'accesstoken': Get_token(),
        'title': 'xxxxxxxxxxxxxxxxxx',
        'tab': 'ask',
        'topic_id':topic_id,
        'content': '77777'
    }
    # topic_id = Create_topic(data)

    res = requests.post(url=url,data=update_data).json()

    #更新后的id判断
    update_topicid = res['topic_id']
    assert  topic_id == update_topicid
    #获取更新后的内容
    res1 = Get_topic_detail(update_topicid).json()

    assert update_data['title'] == res1['data']['title']
    assert update_data['tab'] == res1['data']['tab']
    assert update_data['content'] in res1['data']['content']
    # return res1

def test_topic_collect():
    """
    收藏主题
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    topic_id = Create_topic(data)

    url = defaulturl+'/topic_collect/collect'
    logger.debug(f'发送请求：{url}')

    topic_data = {
        'accesstoken':accesstoken,
        'topic_id':topic_id
    }
    res = requests.post(url=url,data=topic_data).json()
    assert res['success'] == True

def test_topic_decollect():
    """
    取消收藏
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    topic_id = Create_topic(data)
    #收藏主题
    url = defaulturl + '/topic_collect/collect'
    logger.debug(f'发送请求：{url}')

    topic_data = {
        'accesstoken': accesstoken,
        'topic_id': topic_id
    }
    res = requests.post(url=url, data=topic_data).json()
    assert res['success'] == True
    #取消收藏主题
    url = defaulturl + '/topic_collect/de_collect'
    logger.debug(f'发送请求：{url}')

    topic_data = {
        'accesstoken': accesstoken,
        'topic_id': topic_id
    }
    res1 = requests.post(url=url, data=topic_data).json()
    assert res1['success'] == True

def test_user_collect():
    """
    用户所收藏的主题
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    username = Get_username(data)
    url = defaulturl + '/topic_collect/' + username
    logger.debug(f'发送请求：{url}')
    res = requests.get(url=url).json()
    assert res['success'] == True

def test_create_common():
    """
    新建评论
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    topic_id = Create_topic(data)
    url = defaulturl+'/topic/'+ topic_id + '/replies'
    logger.debug(f'发送请求：{url}')

    parmas = {
        'accesstoken':Other_token(),
        'content':'666666'
    }
    res = requests.post(url=url,data=parmas).json()
    assert res['success'] == True

def test_reply_common():
    """
    回复已有评论
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    #拿到新建帖子ID
    topic_id = Create_topic(data)
    url = defaulturl + '/topic/' + topic_id + '/replies'
    logger.debug(f'发送请求：{url}')

    #新建评论
    replydata ={
        'accesstoken': Other_token(),
        'content': '666666'
    }
    #获取评论ID
    reply_id = Get_reply_id(topic_id,replydata)
    parmas = {
        'accesstoken': Get_token(),
        'content': '9999',
        'reply_id':reply_id
    }
    #根据reply_id回复已有评论
    res = requests.post(url=url, data=parmas).json()
    assert parmas['reply_id'] != res['reply_id']

def test_thump():
    """
    为评论点赞
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    # 拿到新建帖子ID
    topic_id = Create_topic(data)

    # 新建评论
    replydata = {
        'accesstoken': Other_token(),
        'content': '666666'
    }
    # 获取评论ID
    reply_id = Get_reply_id(topic_id, replydata)
    url = defaulturl + '/reply/' + reply_id + '/ups'
    logger.debug(f'发送请求：{url}')
    thumpdata = {
        'accesstoken':Get_token()
    }
    res = requests.post(url=url,data=thumpdata).json()
    res1 = requests.post(url=url,data=thumpdata).json()
    assert res['action'] != res1['action']

def test_user_detail():
    """
    获取用户详情
    :return:
    """
    data = {
        'accesstoken': Get_token(),
        'title': 'hello',
        'tab': 'ask',
        'content': '666666'
    }
    username = Get_username(data)
    url = defaulturl + '/user/' + username
    logger.debug(f'发送请求：{url}')
    res = requests.get(url=url).json()['data']['loginname']
    assert username == res

def test_verfily_token():
    """
    验证accesstoken
    :return:
    """
    data = {
        'accesstoken':Get_token()
    }
    url1 = defaulturl+'/accesstoken'

    res1 = requests.post(url=url1,data=data).json()
    url = defaulturl+'/accesstoken'
    logger.debug(f'发送请求：{url}')
    res = Get_verfily_token(url,data)
    assert res[0] == res1['success']
    assert res[1] == res1['loginname']
    assert res[2] == res1['id']

def test_hasnot_messsagess():
    """
    获取未读消息计数
    :return:
    """
    data = {
        'accesstoken':Get_token()
    }
    url = defaulturl+'/message/count'
    logger.debug(f'发送请求：{url}')
    res1 = Get_hasnot_number(url,data)
    res = requests.get(url=url,data=data).json()
    assert res1[0] == res['success']
    assert res1[1] == res['data']

def test_detail_allmessages():
    """
    获取已读|未读消息各多少
    :return:
    """
    data = {
        'accesstoken': Get_token()
    }
    url = defaulturl + '/messages'
    logger.debug(f'发送请求：{url}')
    res1 = Get_allmessageNum(url, data)
    res = requests.get(url=url, data=data).json()
    read = len(res['data']['has_read_messages'])
    notread = len(res['data']['hasnot_read_messages'])
    assert read == res1[0]
    assert notread == res1[1]
    # return res

def test_markPartMessages():
    """
    标记某条（片段）消息已读
    :return:
    """
    data = {
        'accesstoken': Get_token()
    }
    id = Get_markPartMessage(data)
    url = defaulturl+'/message/mark_one/'+id
    logger.debug(f'发送请求：{url}')
    res = requests.post(url=url,data=data).json()
    assert res['marked_msg_id'] == id
    # return id

def test_allMarkMessages():
    """
    标记消息全部已读
    :return:
    """
    # data = {
    #     'accesstoken': Get_token()
    # }
    # url = defaulturl+'/message/mark_all'
    pass

# print(test_markPartMessage())
# print(test_detail_allmessages())
# print(test_hasnot_message())
# print(test_verfily_token())
# print(test_thump())
# print(test_user_collect())
# print(test_reply_common())
# print(test_user_detail())

# print(test_View_topic()['data']['author']['loginname'])
# print(test_editor_topic()['data']['title'])
# def level(n):
#      for i in range(1, n + 1):
#         print(" " * (n - (i - 1)) + "*" * (2 * i - 1))
#
# level(4)