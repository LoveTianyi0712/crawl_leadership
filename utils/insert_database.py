# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 10:56
# @Author  : Gan Liyifan
# @File    : insert_database.py
import pymysql
from Config import Config


def insert_leadership(leadership_list):
    # SQL Connection
    conn = pymysql.connect(
        host=Config.DB_HOST,
        port=Config.DB_PORT,
        user=Config.DB_USER,
        password=Config.DB_PASSWORD,
        database=Config.DB_NAME,
        charset=Config.DB_CHARSET,
        connect_timeout=Config.DB_CONNECT_TIMEOUT
    )

    cur = conn.cursor()

    # Create table
    cur.execute('''
            CREATE TABLE `info_leader_appoint` (
                `id` bigint(20) NOT NULL AUTO_INCREMENT COMMENT 'ID',
                `name` varchar(128) DEFAULT '' COMMENT '名字',
                `gender` varchar(30) DEFAULT '' COMMENT '性别',
                `race` varchar(30) DEFAULT '' COMMENT '民族',
                `birthdate` varchar(50) DEFAULT '' COMMENT '出生日期',
                `political_status` varchar(50) DEFAULT '' COMMENT '政治面貌',
                `education` varchar(50) DEFAULT '' COMMENT '学历',
                `current_pos` text COMMENT '现任职务',
                `prepare_pos` text COMMENT '拟任职务',
                `del_flag` char(1) DEFAULT '0' COMMENT '删除标志（0代表存在 2代表删除）',
                `create_by` varchar(64) DEFAULT '' COMMENT '创建者',
                `create_time` datetime DEFAULT NULL COMMENT '创建时间',
                `update_by` varchar(64) DEFAULT '' COMMENT '更新者',
                `update_time` datetime DEFAULT NULL COMMENT '更新时间',
                `remark` varchar(500) DEFAULT NULL COMMENT '备注',
                `url` varchar(512) DEFAULT NULL COMMENT '链接',
                `original_json` text DEFAULT NULL COMMENT '原始json串',
                PRIMARY KEY (`id`)
                ) ENGINE=InnoDB AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb4 COMMENT='领导干部公示信息表';
        ''')

    # Insert data into database
    for leadership in leadership_list:
        cur.execute('''
            INSERT INTO info_leader_appoint (name, gender, race, birthdate, political_status, education, current_pos, prepare_pos, del_flag, create_by, create_time, update_by, update_time, remark, url, original_json)
            VALUES (%(name)s, %(gender)s, %(race)s, %(birthdate)s, %(political_status)s, %(education)s, %(current_pos)s, %(prepare_pos)s, %(del_flag)s, %(create_by)s, %(create_time)s, %(update_by)s, %(update_time)s, %(remark)s, %(url)s, %(original_json)s)
        ''', leadership.to_dict())

    # Commit the query
    conn.commit()

    # Close the database connections
    cur.close()
    conn.close()
