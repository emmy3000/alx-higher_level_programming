#!/usr/bin/env python3
"""
Module: 2-my_filter_states
Description: Connects to a MySQL server and retrieves states from a database
             based on the provided state name argument.
"""

import sys
import MySQLdb


def filter_states(username, password, database, state_name):
    """
    Connects to a MySQL server and retrieves states from the specified database
    where the name matches the provided state_name argument.

    Args:
        username (str): The username for the MySQL server.
        password (str): The password for the MySQL server.
        database (str): The name of the database.
        state_name (str): The name of the state to search for.

    Returns:
        None
    """
    connection = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        passwd=password,
        db=database
    )

    cursor = connection.cursor()

    sql = """
        SELECT id, name
        FROM states
        WHERE name = '{}'
        ORDER BY id ASC
        LIMIT 1
    """.format(state_name)

    cursor.execute(sql)

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    connection.close()


def main():
    """
    Entry point of the script.
    Parses command-line arguments and calls the filter_states function.
    """
    if len(sys.argv) != 5:
        print("Usage: python3 2-my_filter_states.py <username> <password> "
              "<database> <state_name>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    filter_states(username, password, database, state_name)


if __name__ == "__main__":
    main()
