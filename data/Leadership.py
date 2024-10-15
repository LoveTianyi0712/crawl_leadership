# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 9:42
# @Author  : Gan Liyifan
# @File    : Leadership.py
from datetime import datetime


class Leadership:
    def __init__(self, name, gender, race, birthdate, political_status, education, current_pos, prepare_pos):
        self.name = name
        self.gender = gender
        self.race = race
        self.birthdate = birthdate
        self.political_status = political_status
        self.education = education
        self.current_pos = current_pos
        self.prepare_pos = prepare_pos
        self.del_flag = '0'
        self.create_by = '系统定时任务'
        self.create_time = datetime.now()
        self.update_by = ''
        self.update_time = ''
        self.remark = ''
        self.url = ''
        self.original_json = ''

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "race": self.race,
            "birthdate": self.birthdate,
            "political_status": self.political_status,
            "education": self.education,
            "current_pos": self.current_pos,
            "prepare_pos": self.prepare_pos,
            "del_flag": self.del_flag,
            "create_by": self.create_by,
            "create_time": self.create_time,
            "update_by": self.update_by,
            "update_time": self.update_time,
            "remark": self.remark,
            "url": self.url,
            "original_json": self.original_json
        }
