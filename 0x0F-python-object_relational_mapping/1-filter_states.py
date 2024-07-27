#!/usr/bin/python3
"""script that lists all states with a name starting with N"""
import re
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("SELECT * FROM states ORDER BY states.id ASC")
    records = cur.fetchall()

    for row in records:
        if re.findall('^N.+', row[1]) != []:
            print("{}".format(row))
