#!/usr/bin/python3
"""Script that lists all cities from the database"""

from sys import argv
from MySQLdb import connect

if __name__ == '__main__':

    db = connect(host='localhost',
                 port=3306,
                 user=argv[1],
                 passwd=argv[2],
                 db=argv[3])

    cur = db.cursor()
    query = """SELECT cities.id, cities.name, states.name
    FROM cities
    INNER JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """
    cur.execute(query)
    for row in cur.fetchall():
        print("{}".format(row))
