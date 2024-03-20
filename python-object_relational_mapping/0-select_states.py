#!/usr/bin/python3
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
