#!/usr/bin/python3
""""""
import MySQLdb
import sys
import re

if __name__ == '__main__':
    uname, passwd, dbn = sys.argv[1], sys.argv[2], sys.argv[3]
    db = MySQLdb.\
        connect(host='localhost', port=3306, user=uname, passwd=passwd, db=dbn)

    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cur.fetchall()
    pattern = '^N.+'
    for row in records:
        if re.findall(pattern, row[1]):
            print("{}".format(row))
