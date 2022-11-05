import mysql.connector
import os
import sys

BASE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(BASE_PATH, 'config'))
import mysqldb

with mysql.connector.connect(
    user = mysqldb.user, 
    password = mysqldb.password,
    host = mysqldb.host,
    database = mysqldb.database
) as connection:  
    create_db_query = '''
        CREATE TABLE IF NOT EXISTS `message` (
            id         BIGINT AUTO_INCREMENT,
            member_id  BIGINT NOT NULL,
            content    VARCHAR(255) NOT NULL,
            like_count INT UNSIGNED NOT NULL DEFAULT 0,
            `time`     DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id),
            FOREIGN KEY (member_id) REFERENCES member(id)
        )
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)