# -*- coding: utf-8 -*-
# @Time    : 2024/10/15 9:05
# @Author  : Gan Liyifan
# @File    : Config.py

# Project configuration
class Config:
    # database configuration
    DB_HOST = 'localhost'
    DB_PORT = 3306
    DB_USER = 'root'
    DB_PASSWORD = 'root'
    DB_NAME = 'test'
    DB_CHARSET = 'utf8mb4'
    DB_CONNECT_TIMEOUT = 10

    # AI configuration
    AI_API = 'YOUR AI API here'

    # time configuration (Note that the kimi free api can only access 3 times per minute)
    TIME_INTERVAL = 30

    # config the time period of crawling
    CRAWL_PERIOD = 7
