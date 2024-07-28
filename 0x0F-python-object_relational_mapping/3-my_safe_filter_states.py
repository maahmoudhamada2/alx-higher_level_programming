#!/usr/bin/python3
"""Script that takes in arguments and displays all values in the states"""
import re
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    query = "SELECT * FROM states WHERE name=%s ORDER BY states.id ASC"
    cur.execute(query, (argv[4],))
    records = cur.fetchall()
    for row in records:
        if row[1] == argv[4]:
            print("{}".format(row))
