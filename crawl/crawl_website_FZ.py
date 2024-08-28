# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 10:48
# @Author  : Gan Liyifan
# @File    : crawl_website_FZ.py
import re
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content


def crawl_website_FZ(period):
    url = "http://www.jxfz.gov.cn/col/col24619/index.html#div"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')
        scripts = soup.find_all('script', type='text/xml')

        for script in scripts:
            cdata_content = script.string
            matches = re.findall(r'<li>.*?</li>', cdata_content, re.DOTALL)

        for li in matches:
            li_soup = BeautifulSoup(li, 'html.parser')
            link = "https://www.jxfz.gov.cn/" + li_soup.find('a')['href']
            date = li_soup.find('b').text.strip()
            print(link, date)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

url = "https://www.jxfz.gov.cn//art/2024/7/26/art_24619_4201962.html"
paragraphs = get_content(url)
print(paragraphs)
