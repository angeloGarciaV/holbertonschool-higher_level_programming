#!/usr/bin/python3
"""lists all cities of that state from input"""
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""
                USE hbtn_0e_4_usa;
                SELECT cities.name FROM cities
                INNER JOIN states
                ON state_id = states.id
                WHERE states.name LIKE BINARY %s
                ORDER BY cities.id ASC;
                """, {'state_name': argv[4]})
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()