# -*- coding: utf-8 -*-
# @Time    : 2024/8/24 9:42
# @Author  : Gan Liyifan
# @File    : Leadership.py

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

    def to_dict(self):
        return {
            "name": self.name,
            "gender": self.gender,
            "race": self.race,
            "birthdate": self.birthdate,
            "political_status": self.political_status,
            "education": self.education,
            "current_pos": self.current_pos,
            "prepare_pos": self.prepare_pos
        }