#!/usr/bin/python
import psycopg2

conn = psycopg2.connect(database="db_name", user="username",  password="password", host="rds.endpoint.amazonaws.com", port="5432")
cur = conn.cursor()

empty_list = []
cur.execute("select 'ANALYZE '||relname||';' from pg_stat_user_tables where relname in ('table_name1','table_name2');")
row_count = cur.rowcount

if row_count > 0:
    for row in cur:
        empty_list.append(row[0])
        tables = row[0]
        for x in empty_list:
            conn2 = psycopg2.connect(database="db_name", user="username",  password="password", host="rds.endpoint.amazonaws.com", port="5432")
            cur2 = conn2.cursor()
            cur2.execute(x)
            conn2.close()
            
