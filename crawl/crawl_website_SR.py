# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 8:47
# @Author  : Gan Liyifan
# @File    : crawl_website_SR.py
import requests
from bs4 import BeautifulSoup
from utils.get_data import get_content


def crawl_website_SR(period):

    url = "https://www.zgsr.gov.cn/zgsr/rsrm/zwgk_xxgklist.shtml"
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
            if li.find('div', class_='zcwj-wj') and li.find('span', class_='span_date'):
                link = 'https://www.zgsr.gov.cn' + li.find('a', href=True)['href']
                date = li.find('span', class_='span_date').text
                print(link, date)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

url = 'https://www.zgsr.gov.cn/cgj/rsrm/202408/bbdfbd0994c74b5eb0d3de0e43fd8d2d.shtml'
paragraphs = get_content(url)
print(paragraphs)