# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 13:51
# @Author  : Gan Liyifan
# @File    : crawl_website_JDZ.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_JDZ(period):
    url = "https://www.jdz.gov.cn/zwgk/fdzdgknr/rsxx/rsrm/"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        print(response.text)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

crawl_website_JDZ(7) ## TODO
