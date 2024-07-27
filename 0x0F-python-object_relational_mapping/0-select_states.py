#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    uname = sys.argv[1]
    passwd = sys.argv[2]
    dbn = sys.argv[3]
    db = MySQLdb.\
        connect(host='localhost', port=3306, user=uname, passwd=passwd, db=dbn)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cur.fetchall()
    for row in records:
        print(row)
