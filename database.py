import pymysql

import os
timeout = 10
connection = pymysql.connect(
    charset="utf8mb4",
    connect_timeout=timeout,
    cursorclass=pymysql.cursors.DictCursor,
    db = os.environ['db'],
    host = os.environ['host'],
    password = os.environ['password'],
    read_timeout = timeout,
    port = int(os.environ['port']),
    user = os.environ['user'],
    write_timeout = timeout,
)
