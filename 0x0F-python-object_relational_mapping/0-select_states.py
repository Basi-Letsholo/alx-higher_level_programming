#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa. """


import MySQLdb
import sys

if __name__ == '__main__':

    username = sys.argv[1]
    user_password = sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(
            host='localhost',
            user=username,
            password=user_password,
            db=db_name,
            port=3306
    )

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM states ORDER BY states.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    connection.close()
