#!/usr/bin/env python3
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
    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=mysql_user,
            passwd=mysql_password,
            db=database_name
            )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to get all states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Filter out duplicate states using Python
    unique_states = []
    seen_states = set()
    for row in rows:
        state = row[1]
        if state not in seen_states:
            unique_states.append(row)
            seen_states.add(state)

    # Close the cursor and database connection
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

    # Retrieve unique states from the database
    states = retrieve_states(mysql_user, mysql_password, database_name)

    # Print the states in the desired format.
    for state in states:
        print(state)


if __name__ == "__main__":
    main()
