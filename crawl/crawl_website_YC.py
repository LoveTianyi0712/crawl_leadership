# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 12:07
# @Author  : Gan Liyifan
# @File    : crawl_website_YC.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_YC(period):
    url = "http://www.yichun.gov.cn/ycsrmzf/rsrm/xxgk_list.shtml"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')
        li_tags = soup.find_all('li')
        for li in li_tags:
            if li.find('a') and 'target' in li.find('a').attrs and 'title' in li.find('a').attrs:
                link = 'http://www.yichun.gov.cn' + li.find('a')['href']
                pub_time = li.find('span', class_='time').text
                print(link, pub_time)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

url = "http://www.yichun.gov.cn/ycsrmzf/rsrm/202405/6c6e706cf5d44db0840bcbb9051eaafb.shtml"
paragraph = get_content(url)
print(paragraph)
