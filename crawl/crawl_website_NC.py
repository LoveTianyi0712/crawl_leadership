# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 14:27
# @Author  : Gan Liyifan
# @File    : crawl_website_NC.py
import time

import requests
from bs4 import BeautifulSoup
from datetime import datetime

from utils.ai_processing import ai_processing, ai_processing_simple
from utils.get_data import get_content


def crawl_website_NC(period):

    url = "http://www.nc.gov.cn/ncszf/rsrm1/2021zfxxgk_list.shtml"
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
            if li.find('a') and 'target' in li.find('a').attrs and 'title' in li.find('a').attrs:
                link = 'http://www.nc.gov.cn' + li.find('a')['href']
                pub_date_str = li.find('span', class_='time').text
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
