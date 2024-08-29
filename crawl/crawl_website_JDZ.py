# -*- coding: utf-8 -*-
# @Time    : 2024/8/28 13:51
# @Author  : Gan Liyifan
# @File    : crawl_website_JDZ.py
import requests
from bs4 import BeautifulSoup

from utils.get_data import get_content

def crawl_website_JDZ(period):
    url = "https://www.jdz.gov.cn/zwgk/fdzdgknr/rsxx/rsrm/index_1.shtml"
    headers = {
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Encoding": "gzip, deflate, br, zstd",
        "Accept-Language": "zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6",
        "Content-Type": "application/json; charset=UTF-8",
        "Cookie": "arialoadData=false; FW9uCWqlVzC22m1KfCMCjfvFHpRMsgt=15ff4e2e-d28b-47c6-acba-7403d12a695e; JSESSIONID=16D25324811D11EBA9B85313064E09D4; _trs_ua_s_1=m0dftq07_4448_4u27; _trs_uv=m0dftq08_4448_4nrp",
        "Origin": "https://www.jdz.gov.cn",
        "Referer": "https://www.jdz.gov.cn/zwgk/fdzdgknr/rsxx/rsrm/index_1.shtml",
        "Sec-CH-UA": '"Chromium";v="128", "Not;A=Brand";v="24", "Microsoft Edge";v="128"',
        "Sec-CH-UA-Mobile": "?0",
        "Sec-CH-UA-Platform": '"Windows"',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36 Edg/128.0.0.0",
    }

    response = requests.get(url, headers=headers)
    if response.status_code == 200:
        response.encoding = "utf-8"
        print(response.text)

    else:
        raise (ConnectionError("Fail to response, status code: ", response.status_code))

crawl_website_JDZ(7) ## TODO
