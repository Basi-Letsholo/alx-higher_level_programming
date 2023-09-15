#!/usr/bin/python3
"""Lists all cities from the database hbtn_0e_4_usa."""


import MySQLdb
import sys

if __name__ == '__main__':

    if len(sys.argv) != 4:
        print('Usage: ./4-cities_by_state.py username password database')
        sys.exit(1)

    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    connection = MySQLdb.connect(
            host='localhost',
            user=mysql_username,
            password=mysql_password,
            db=db_name,
            port=3306
    )

    cursor = connection.cursor()

    query = "SELECT cities.id, cities.name, states.name FROM cities "
    query += "LEFT JOIN states ON cities.state_id = states.id "
    query += "ORDER BY cities.id ASC"

    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    connection.close()
