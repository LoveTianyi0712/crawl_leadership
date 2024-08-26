# -*- coding: utf-8 -*-
# @Time    : 2024/8/23 12:50
# @Author  : Gan Liyifan
# @File    : get_data.py

import requests
import re
import datetime
from bs4 import BeautifulSoup
from data.Leadership import Leadership


def get_leadership(url):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/127.0.0.0 Safari/537.36 Edg/127.0.0.0"
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        response.encoding = "utf-8"
        soup = BeautifulSoup(response.text, 'html.parser')

        p_labels = soup.find_all('p')
        pub_date_tag = soup.find('meta', {'name': 'pubdate'})

        # Convert all the labels into paragraphs
        paragraphs = []
        for label in p_labels:
            paragraphs.append(label.text)

        # Convert the publication date into tags
        if pub_date_tag:
            pub_date_str = pub_date_tag.get('content')
            time_obj = datetime.datetime.strptime(pub_date_str, "%Y-%m-%d %H:%M")
            pub_date = time_obj.date()
        else:
            raise (ValueError("Publication date not found. Please check the website manually"))

        return paragraphs, pub_date
    else:
        return -1


def retrieve_leadership(paragraphs):
    leaderships = []
    for paragraph in paragraphs:
        info_list = paragraph.split("，")
        if len(info_list) >= 8:
            leadership = convert_leadership(info_list)
            leaderships.append(leadership)

    return leaderships


def convert_leadership(info_list):
    l_name = info_list[0]
    l_gender = info_list[1]
    l_race = info_list[2]

    pattern = r'(\d{4})年(0?[1-9]|1[0-2])月(.+)'
    match = re.match(pattern, info_list[3])

    if match:
        year = int(match.group(1))
        month = int(match.group(2))
        formatted_date = datetime.date(year, month, 1).strftime('%Y-%m')
    else:
        raise (ValueError("Invalid date time format while processing the birthdate:", info_list[3]))

    l_birthdate = formatted_date

    l_political_status = info_list[4]
    l_education = info_list[5]

    current_pos = info_list[6:-1]
    l_current_pos = current_pos

    prepare_pos = info_list[-1][:-1]
    l_prepare_pos = prepare_pos

    return Leadership(l_name, l_gender, l_race, l_birthdate, l_political_status,
                      l_education, l_current_pos, l_prepare_pos)
