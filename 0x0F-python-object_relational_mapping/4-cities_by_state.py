#!/usr/bin/python3
""" Lists all cities from the database hbtn_0e_4_usa
Script takes 3 arguments"""

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
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states ON states.id = cities.state_id
        ORDER BY states.id ASC"""
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    conn.close()
