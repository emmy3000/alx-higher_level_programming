#!/usr/bin/python3
"""
This script retrieves all states from the hbtn_0e_0_usa database.

Usage: python3 get_states.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306 and
displays the states in ascending order by their ID.
"""

import MySQLdb
import sys


def retrieve_states(mysql_user, mysql_password, database_name):
    """
    Retrieve all unique states from the hbtn_0e_0_usa database.

    Args:
        mysql_user (str): MySQL username.
        mysql_password (str): MySQL password.
        database_name (str): Name of the database.

    Returns:
        list: List of tuples representing the retrieved states.
    """
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )

    cursor = db.cursor()

    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()

    return unique_states


def main():
    """
    Entry point of the script.
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

    states = retrieve_states(mysql_user, mysql_password, database_name)

    for state in states:
        print(state)


if __name__ == "__main__":
    main()
