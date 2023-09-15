#!/usr/bin/python3
"""Displays values in state matching state argument & safe from injections."""

import MySQLdb
import sys

if __name__ == '__main__':

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    connection = MySQLdb.connect(
            host='localhost',
            user=mysql_username,
            password=mysql_password,
            db=db_name,
            port=3306
    )

    cursor = connection.cursor()

    query = "SELECT * FROM states WHERE states.name = %s "
    query += "ORDER BY states.id ASC"

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
