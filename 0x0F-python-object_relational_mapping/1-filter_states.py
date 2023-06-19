#!/usr/bin/env python3
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
    # Retrieve command line arguments
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Create and execute the SQL query
    query = """
        SELECT id, name
        FROM states
        WHERE name LIKE 'N%'
        ORDER BY id ASC
        LIMIT 2
    """
    cursor.execute(query)

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
