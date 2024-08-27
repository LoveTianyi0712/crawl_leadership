# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 8:46
# @Author  : Gan Liyifan
# @File    : crawl_website_JJ.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime

from utils.ai_processing import ai_processing
from utils.get_data import get_content


def crawl_website_JJ(period):

    url = "https://www.jiujiang.gov.cn/xxgk/xzwgk/glgk/rsxx/rsrm/index_mo.html"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')
        items = soup.find_all('li', class_='item')
        leadership_list = []
        for item in items:

            link = item.find('a')['href']
            text_part = item.find('div', class_='text-part')

            if text_part:
                pub_date_str = text_part.find('span', class_='time').text
                time_obj = datetime.strptime(pub_date_str, "%Y-%m-%d %H:%M:%S")
                pub_date = time_obj.date()
                current_date = datetime.now().date()
                time_diff = current_date - pub_date
                if period > time_diff.days:
                    paragraphs = get_content(link)
                    leaderships = ai_processing(paragraphs)
                    leadership_list.extend(leaderships)

        return leadership_list

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))
