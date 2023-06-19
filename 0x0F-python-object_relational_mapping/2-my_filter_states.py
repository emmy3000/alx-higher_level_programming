#!/usr/bin/python3
"""
This script connects to a MySQL server and displays all rows
in the states table where the name matches the provided argument.

Usage:
    ./2-my_filter_states.py <mysql_username> \
                            <mysql_password> \
                            <database_name> \
                            <state_name_searched>
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

    sql = """
        SELECT id, name FROM states
        WHERE name = BINARY '{}'
        ORDER BY id ASC
    """.format(state_name)
    cursor.execute(sql)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
