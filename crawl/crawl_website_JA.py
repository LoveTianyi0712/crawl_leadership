# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 9:12
# @Author  : Gan Liyifan
# @File    : crawl_website_JA.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content


def crawl_website_JA(period):
    url = "https://www.jian.gov.cn/api-ajax_list-1.html"

    headers = {
        "authority": "www.jian.gov.cn",
        "method": "POST",
        "path": "/api-ajax_list-1.html",
        "scheme": "https",
        "accept": "application/json, text/javascript, */*; q=0.01",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
        "origin": "https://www.jian.gov.cn",
        "referer": "https://www.jian.gov.cn/xxgk-list-rsrm.html",
        "sec-ch-ua": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"Windows"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
        "x-requested-with": "XMLHttpRequest",
    }

    data = {
        "ajax_type[]": [
            "21_xxgk",
            "166000",
            "21",
            "xxgk",
            "Y-m-d",
            "50",
            "20",
            [
                "is_top DESC",
                "displayorder DESC",
                "inputtime DESC"
            ],
            ""
        ],
        "is_ds": "1"
    }

    response = requests.post(url, headers=headers, data=data)
    if response.status_code == 200:
        json_data = response.json()
        items = json_data["data"]
        for item in items:
            link = item["url"]
            update_time = item["updatetime"]
            print(link, update_time)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))


url = "http://www.jian.gov.cn/xxgk-show-10224468.html"
paragraphs = get_content(url)
print(paragraphs)
