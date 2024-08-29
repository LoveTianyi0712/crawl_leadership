# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 9:12
# @Author  : Gan Liyifan
# @File    : crawl_website_JA.py
import time
from datetime import datetime

import requests

from utils.ai_processing import ai_processing_simple
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
    leadership_list = []
    if response.status_code == 200:
        json_data = response.json()
        items = json_data["data"]
        for item in items:
            link = item["url"]
            pub_date_str = item["updatetime"]
            time_obj = datetime.strptime(pub_date_str, "%Y-%m-%d")
            pub_date = time_obj.date()
            current_date = datetime.now().date()
            time_diff = current_date - pub_date
            if period > time_diff.days:
                print(link)
                paragraphs = get_content(link)
                leaderships = ai_processing_simple(paragraphs)
                time.sleep(20)
                leadership_list.extend(leaderships)

        return leadership_list

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

crawl_website_JA(30) ## TODO
## Pdf problem