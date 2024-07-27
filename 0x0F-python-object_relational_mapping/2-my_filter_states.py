#!/usr/bin/python3
"""Script that takes in an argument and displays all values in the states"""

import MySQLdb
import sys

if __name__ == '__main__':
    uname = sys.argv[1]
    passwd = sys.argv[2]
    dbn = sys.argv[3]
    value = sys.argv[4]
    db = MySQLdb.\
        connect(host='localhost', port=3306, user=uname, passwd=passwd, db=dbn)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}'".format(value))
    records = cur.fetchall()
    for row in records:
        print("{}".format(row))
