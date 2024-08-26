# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 9:25
# @Author  : Gan Liyifan
# @File    : crawl.py

import requests
import re
from get_data import get_leadership, retrieve_leadership
from bs4 import BeautifulSoup
from datetime import datetime


def crawl_website_JX(period):
    url = "https://sousuo.jiangxi.gov.cn/jsearchfront/interfaces/cateSearch.do"

    data = {
        "websiteid": "360000000000000",
        "searchid": "981",
        "pg": "",
        "p": 1,
        "tpl": "49",
        "sortType": "2",
        "q": "领导干部任前公示",
        "pq": "",
        "oq": "",
        "eq": "",
        "pos": "title",
        "od": "2",
        "begin": "",
        "end": ""
    }

    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Connection": "keep-alive",
        "Content-Type": "application/x-www-form-urlencoded",
        "Host": "sousuo.jiangxi.gov.cn",
        "Origin": "https://sousuo.jiangxi.gov.cn",
        "Referer": url,
        "Sec-CH-UA": "\"Not)A;Brand\";v=\"99\", \"Microsoft Edge\";v=\"127\", \"Chromium\";v=\"127\"",
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": "\"Windows\"",
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0",
        "X-Requested-With": "XMLHttpRequest"
    }

    response = requests.post(url, headers=headers, data=data)

    if response.status_code == 200:
        json_data = response.json()
        result_list = json_data.get('result', [])
        leadership_list = []
        for item in result_list:
            soup = BeautifulSoup(item, "html.parser")
            links = soup.find_all("a", href=True)
            url_pattern = r'http[s]?://[^ ]+'
            url_match = re.search(url_pattern, links[1].text)
            clean_url = url_match.group(0).strip()
            paragraphs, pub_date = get_leadership(clean_url)

            if paragraphs == -1:
                raise (ConnectionError("Failed to get data at", clean_url))

            current_date = datetime.now().date()
            time_diff = current_date - pub_date
            if period > time_diff.days:
                leaderships = retrieve_leadership(paragraphs)
                leadership_list.extend(leaderships)

        return leadership_list
    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))
