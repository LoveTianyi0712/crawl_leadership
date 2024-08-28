# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 13:53
# @Author  : Gan Liyifan
# @File    : crawl_website_YT.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_YT(period):
    url = ("http://www.yingtan.gov.cn/module/xxgk/search.jsp?divid=div4&infotypeId=Y50003Y50005Y50001&jdid=1&area"
           "=&standardXxgk=1")
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
            link = li.find('a')['href']
            pub_time = li.find('b').text
            print(link, pub_time)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

url = "http://www.yingtan.gov.cn/art/2024/8/26/art_12609_1422498.html?xxgkhide=1"
paragraphs = get_content(url)
print(paragraphs)