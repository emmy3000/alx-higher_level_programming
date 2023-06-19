#!/usr/bin/python3
"""
This script connects to a MySQL server and lists all states
with a name starting with `N` from the specified database.

Usage:
    ./1-filter_states.py <mysql_username> \
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
        SELECT id, name
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
    """
    cursor.execute(query)
    rows = cursor.fetchall()
    unique_rows = set()
    filtered_rows = []

    for row in rows:
        if row not in unique_rows:
            filtered_rows.append(row)
            unique_rows.add(row)

    for row in filtered_rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
