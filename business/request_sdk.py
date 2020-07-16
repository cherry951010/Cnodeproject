import requests

from business.logger import logger

def do_requests(url,method:str,params=None,data=None):
    method = method.lower()
    if method == 'get':
        logger.debug(f'{url} {method} {params}')
        res = requests.get(url=url,params=params)
        logger.debug(f'{res.text} {res.status_code} {res.elapsed.total_seconds()}s')
        return res
    elif method == 'post':
        logger.debug(f'{url} {method} {params}')
        res = requests.get(url=url, params=params)
        logger.debug(f'{res.text} {res.status_code} {res.elapsed.total_seconds()}s')
        return res
    else:
        logger.error(f'check http request method {method}')