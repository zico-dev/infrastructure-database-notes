#!/usr/bin/python
import psycopg2
import time
conn = psycopg2.connect(database="Test_DB", user="zicky",  password="test1234", host="postgresql.rdsendpoint.us-east-1.rds.amazonaws.com", port="5432")

cur = conn.cursor()
current_time = time.strftime("%H:%M:%S")
cur.execute("select pid, state, query, usename, datname, to_char(query_start, 'DD Mon YYYY HH24:MI:SS') from pg_stat_activity where state='idle in transaction';")
f = open('/home/ec2-user/success.log', 'w')
counter = 0
header = '{:>20} {:>20} {:>25} {:>20} {:>20} {:>23} '.format("PID", "Query State", "Query", "Username", "Database Name", "Query Start Time")
f.write("We found locks in the Database:" + '\n')
f.write(header)
def db_locks():
    x = counter
    for row in cur:
            x +=  1
            f.write('\n')
            format_output = '{:>20} {:>20} {:>25} {:>20} {:>20} {:>23} '.format(str(row[0]), str(row[1]), str(row[2]), str(row[3]), str(row[4]), str(row[5]))
            f.write(format_output)
    f.write('\n')
    f.write('%s Database lock(s) were found on ' %(x) + str(current_time) + '\n' )
    return
db_locks()
