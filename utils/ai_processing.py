# -*- coding: utf-8 -*-
# @Time    : 2024/8/27 9:27
# @Author  : Gan Liyifan
# @File    : ai_processing.py
from openai import OpenAI
from utils.get_data import convert_leadership
from data.Leadership import Leadership


def ai_processing(paragraphs):
    api = "Your api here"
    content = '''
              提取领导任免职信息，按照"姓名;性别;民族;出生年月;学历;政治面貌;现任职务;拟任/免职务。"字段排列
              只输出指定内容，不要输出其他多余内容，不存在字段写"不详"，免去职务在"拟任/免职务"标注免去
              '''

    client = OpenAI(
        api_key=api,
        base_url="https://api.moonshot.cn/v1",
    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": content},
            {"role": "user", "content": paragraphs},
        ],
        temperature=0.3,
    )

    leaderships = []
    results = completion.choices[0].message.content
    results = results.split("\n")
    for result in results:
        info_list = result.split(";")
        leaderships.append(convert_leadership(info_list))

    return leaderships


def ai_processing_simple(paragraphs):
    api = "Your api here"
    content = '''
                  提取领导任免职信息，按照"姓名;职务;[1/-1]"字段排列
                  任职标记1，免职标记-1
                  '''

    client = OpenAI(
        api_key=api,
        base_url="https://api.moonshot.cn/v1",
    )

    completion = client.chat.completions.create(
        model="moonshot-v1-8k",
        messages=[
            {"role": "system",
             "content": content},
            {"role": "user", "content": paragraphs},
        ],
        temperature=0.3,
    )

    leaderships = []
    results = completion.choices[0].message.content
    results = results.split("\n")
    for result in results:
        info_list = result.split(";")
        if info_list[2] == '1':
            name = info_list[0]
            prepare_pos = info_list[1]
            leaderships.append(
                Leadership(name, "", "", "", "", "", "", prepare_pos)
            )
        elif info_list[2] == '-1':
            name = info_list[0]
            current_pos = info_list[1]
            leaderships.append(
                Leadership(name, "", "", "", "", "", current_pos, "")
            )
        else:
            raise (ValueError("AI may gives a wrong output, please check manually"))

    return leaderships
