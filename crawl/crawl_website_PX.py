# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 12:14
# @Author  : Gan Liyifan
# @File    : crawl_website_PX.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_PX(period):
    url = "http://www.pingxiang.gov.cn/col/col38/index.html?vc_xxgkarea=PX0043&number=P00005"
    headers = {
        'Accept': '*/*',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Connection': 'keep-alive',
        'Content-Length': '7777',
        'Content-Type': 'text/plain',
        'Cookie': 'FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=462ece14-09a8-4f83-a89b-cc454547f201; '
                  'dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpL6qakq0M2klvyQsW4uAo%2Bs%3D; '
                  'dGg2aCfMMK97Ro270mqBFu5qjC8TQbL2opnHvbEpM=Tifz8hd5p4O3AB%2BivrbJpL6qakq0M2klvyQsW4uAo%2Bs%3D; '
                  'FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=462ece14-09a8-4f83-a89b-cc454547f201',
        'Host': 'www.pingxiang.gov.cn',
        'Origin': 'http://www.pingxiang.gov.cn',
        'Referer': 'http://www.pingxiang.gov.cn/col/col38/index.html?vc_xxgkarea=PX0043&number=P00005',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0'
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        print(response.text)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

crawl_website_PX(7) ## TODO
