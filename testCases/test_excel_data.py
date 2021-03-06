import pytest
import requests
import json

from business.common import GetExceldata


test_data = GetExceldata('data/data.xlsx','topics')
@pytest.mark.parametrize('url,method,topic_id,code,msg',test_data)
def test_create_topic(url,method,topic_id,code,msg):
    if method == 'post':
        res = requests.post(url,data=json.loads(topic_id))
        assert res.status_code == code
        print(res.status_code)
        assert res.json() == json.loads(msg)
        print(res.json())
        return res
