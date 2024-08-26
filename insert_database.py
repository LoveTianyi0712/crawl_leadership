# -*- coding: utf-8 -*-
# @Time    : 2024/8/26 10:56
# @Author  : Gan Liyifan
# @File    : insert_database.py
import pymysql


def insert_leadership(leadership_list):
    # SQL Connection
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        password='root',
        database='test',
        charset='utf8mb4',
        connect_timeout=10
    )

    cur = conn.cursor()

    # Create table
    cur.execute('''
            CREATE TABLE IF NOT EXISTS Leadership (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255),
                gender VARCHAR(10),
                race VARCHAR(50),
                birthdate VARCHAR(20),
                political_status VARCHAR(50),
                education VARCHAR(50),
                current_pos TEXT,
                prepare_pos TEXT
            )
        ''')

    # Insert data into database
    for leadership in leadership_list:
        cur.execute('''
            INSERT INTO Leadership (name, gender, race, birthdate, political_status, education, current_pos, prepare_pos)
            VALUES (%(name)s, %(gender)s, %(race)s, %(birthdate)s, %(political_status)s, %(education)s, %(current_pos)s, %(prepare_pos)s)
            ''', leadership.to_dict())

    # Commit the query
    conn.commit()

    # Close the database connections
    cur.close()
    conn.close()
