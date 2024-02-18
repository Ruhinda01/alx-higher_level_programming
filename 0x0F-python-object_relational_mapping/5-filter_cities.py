#!/usr/bin/python3
""" Takes in the name of a state as an argument and
lists all cities of that state using hbtn_0e_4_usa"""

import MySQLdb
import sys

if __name__ == '__main__':
    conn = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3],
            charset="utf8"
            )
    cur = conn.cursor()
    query = """
        SELECT name FROM cities
        WHERE state_id = (SELECT id FROM states WHERE name = %s)
        ORDER BY cities.id ASC"""
    cur.execute(query, (sys.argv[4],))
    rows = cur.fetchall()
    items = []
    for row in rows:
        items.append(row[0])
    cities_str = ", ".join(items)
    print(cities_str)

    cur.close()
    conn.close()
