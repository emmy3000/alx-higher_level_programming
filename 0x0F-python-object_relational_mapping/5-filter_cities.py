#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all cities
of a specific state from the specified database.

Usage:
    ./5-filter_cities.py <mysql_username>  \
                          <mysql_password>  \
                          <database_name>    \
                          <state_name>
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
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    cursor = db.cursor()

    query = """
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """

    cursor.execute(query, (state_name,))

    rows = cursor.fetchall()
    city_names = [row[0] for row in rows]
    print(", ".join(city_names))

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
