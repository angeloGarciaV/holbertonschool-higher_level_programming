#!/usr/bin/python3
""" Takes in an argument and displays all values
    where name matches the argument. Safely"""

import MySQLdb
from sys import argv

srch = argv[4]

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=argv[1],
                         passwd=argv[2], db=argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("""SELECT * FROM states
                WHERE name LIKE %s ORDER BY id ASC""", (srch+'%',))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
