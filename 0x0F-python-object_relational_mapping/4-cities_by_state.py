#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all cities
from the specified database.

Usage:
    ./4-cities_by_state.py <mysql_username> \
                           <mysql_password> \
                           <database_name>
"""

import MySQLdb
import sys


def main():
    """
    Main function of the script.
    """
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.id, cities.name, states.name
        FROM cities
        INNER JOIN states
        ON cities.state_id = states.id
        ORDER BY cities.id ASC
    """
    cursor.execute(query)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
