# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 11:17
# @Author  : Gan Liyifan
# @File    : crawl_website_GZ.py
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from utils.ai_processing import ai_processing_simple
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
        leadership_list = []
        for li in li_tags:
            link = 'https://www.ganzhou.gov.cn' + li.find('a')['href']
            pub_date_str = li.find('span', class_='time').text
            pub_date_str = pub_date_str.strip()
            time_obj = datetime.strptime(pub_date_str, "%Y-%m-%d")
            pub_date = time_obj.date()
            current_date = datetime.now().date()
            time_diff = current_date - pub_date
            if period > time_diff.days:
                paragraphs = get_content(link)
                leaderships = ai_processing_simple(paragraphs)
                time.sleep(20)
                leadership_list.extend(leaderships)

        return leadership_list

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

