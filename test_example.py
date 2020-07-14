import  pytest
@pytest.mark.smoketest
@pytest.mark.apitest
def test_demo1():
    assert True
    print('Success')
@pytest.mark.apitest
def test_haha():
    assert False
@pytest.mark.smoketest
@pytest.mark.apitest
def test_demo2():
    assert True
@pytest.mark.smoketest
@pytest.mark.apitest
def test_demo3():
    assert True
@pytest.mark.smoketest
@pytest.mark.apitest
def test_demo4():
    assert True