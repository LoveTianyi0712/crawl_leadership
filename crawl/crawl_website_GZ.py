# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 11:17
# @Author  : Gan Liyifan
# @File    : crawl_website_GZ.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_GZ(period):
    url = "https://www.ganzhou.gov.cn/zfxxgk/c100280/xxgk_list.shtml"
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
            link = 'https://www.ganzhou.gov.cn' + li.find('a')['href']
            pub_time = li.find('span', class_='time').text
            print(link, pub_time)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

url = "https://www.ganzhou.gov.cn/zfxxgk/c100280/202303/c4bad760c67a4ba5a882764404bd6ed0.shtml"
paragraphs = get_content(url)
print(paragraphs)
