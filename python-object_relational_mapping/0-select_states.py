#!/usr/bin/python3
"""Script that lists all states from the database hbtn_0e_0_usa"""
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost',
                         user= 'root',
                         passwd='',
                         db='hbtn_0e_0_usa')
    cur = db.cursor()
    cur.execute( "SELECT * FROM states")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
