#!/usr/bin/env python3
"""
This script lists all states with a name starting with `N`
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb


def list_states(username, password, database):
    """
    Retrieve and print states starting with 'N' (case-sensitive)
    from the specified database.

    Args:
        username (str): The username for the MySQL server.
        password (str): The password for the MySQL server.
        database (str): The name of the database.

    Returns:
        None
    """
    try:
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
            WHERE name LIKE BINARY 'N%'
            ORDER BY id ASC
        """
        cursor.execute(sql)

        rows = cursor.fetchall()

        # Track unique state names
        unique_states = set()

        for row in rows:
            state_id, state_name = row
            if state_name not in unique_states:
                unique_states.add(state_name)
                print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        sys.exit(1)

    finally:
        if connection:
            connection.close()


def main():
    """
    Entry point for the script.
    """
    if len(sys.argv) != 4:
        print("Usage: python3 list_states.py <username> <password> <database>")
        sys.exit(1)

    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)


if __name__ == "__main__":
    main()
