#!/usr/bin/python3
"""script that takes in an argument and displays all values in the state"""
import re
from sys import argv
from MySQLdb import connect

if __name__ == '__main__':
    db = connect(host='localhost', user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()

    cur.execute("""SELECT * FROM states
        WHERE name = '{}'
        ORDER BY states.id ASC""".format(argv[4]))
    records = cur.fetchall()
    for row in records:
        if argv[4] == row[1]:
            print("{}".format(row))
