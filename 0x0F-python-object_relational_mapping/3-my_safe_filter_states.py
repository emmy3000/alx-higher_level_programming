#!/usr/bin/env python3
"""
This script connects to a MySQL server and displays
all values in the states table where the name matches
the provided argument (safe from SQL injection).

Usage:
    ./3-my_safe_filter_states.py <mysql_username> \
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
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL server
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=mysql_username,
        passwd=mysql_password,
        db=database_name
    )

    # Create a cursor object to execute SQL queries
    cursor = db.cursor()

    # Create and execute the SQL query using parameterized query
    query = """
        SELECT *
        FROM states
        WHERE name = %s
        ORDER BY id ASC
    """
    cursor.execute(query, (state_name,))

    # Fetch all the rows returned by the query
    rows = cursor.fetchall()

    # Display the results
    for row in rows:
        print(row)

    # Close the cursor and the database connection
    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
