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
        CREATE TABLE IF NOT EXISTS member (
            id             BIGINT AUTO_INCREMENT,
            `name`         VARCHAR(255) NOT NULL,
            username       VARCHAR(255) NOT NULL,
            `password`     VARCHAR(255) NOT NULL,
            follower_count INT UNSIGNED NOT NULL DEFAULT 0,
            `time`         DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (id)
        )
    '''
    with connection.cursor() as cursor:
        cursor.execute(create_db_query)
    

