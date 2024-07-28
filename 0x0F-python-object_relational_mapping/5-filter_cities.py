#!/usr/bin/python3
"""Script that takes in the name of a state as an arg and lists all cities"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':

    db = connect(host='localhost',
                 port=3306,
                 user=argv[1],
                 passwd=argv[2],
                 db=argv[3])

    cur = db.cursor()
    query = """SELECT cities.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    WHERE states.name=%s
    ORDER BY cities.id ASC
    """
    cur.execute(query, (argv[4],))
    records = cur.fetchall()
    for row in range(len(records)):
        print(records[row][0], end="")
        if row != len(records) - 1:
            print(", ", end="")
    print("")
