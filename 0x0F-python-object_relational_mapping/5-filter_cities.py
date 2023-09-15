#!/usr/bin/python3
"""Lists cities of the state passed as an argument."""


import MySQLdb
import sys

if __name__ == '__main__':

    if len(sys.argv) != 5:
        print("Usage: ./5-filter_cities.py username password database state")
        sys.exit(1)

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

    query = "SELECT cities.name FROM cities INNER JOIN states "
    query += "ON cities.state_id = states.id WHERE states.name = %s "
    query += "ORDER BY cities.id ASC"

    cursor.execute(query, (state_name,))
    rows = cursor.fetchall()
    output = ''

    for i, row in enumerate(rows):
        output += row[0]

        if i < len(rows) - 1:
            output += ', '

    print(output)

    cursor.close()
    connection.close()
