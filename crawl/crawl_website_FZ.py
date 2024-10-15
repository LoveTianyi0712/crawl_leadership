# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 10:48
# @Author  : Gan Liyifan
# @File    : crawl_website_FZ.py
import re
import time
from datetime import datetime

import requests
from bs4 import BeautifulSoup

from Config import Config
from utils.ai_processing import ai_processing_simple
from utils.get_data import get_content, leadership_process


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
        leadership_list = []

        for script in scripts:
            cdata_content = script.string
            matches = re.findall(r'<li>.*?</li>', cdata_content, re.DOTALL)

        for li in matches:
            li_soup = BeautifulSoup(li, 'html.parser')
            link = "https://www.jxfz.gov.cn/" + li_soup.find('a')['href']
            pub_date_str = li_soup.find('b').text.strip()
            time_obj = datetime.strptime(pub_date_str, "%Y-%m-%d")
            pub_date = time_obj.date()
            current_date = datetime.now().date()
            time_diff = current_date - pub_date
            if period > time_diff.days:
                paragraphs, url_response = get_content(link)
                leaderships = ai_processing_simple(paragraphs)
                leaderships = leadership_process(leaderships, link, url_response)
                time.sleep(Config.TIME_INTERVAL)
                leadership_list.extend(leaderships)

        return leadership_list
    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))
