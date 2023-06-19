#!/usr/bin/python3
"""
This script retrieves all states from the `hbtn_0e_0_usa` database.

Usage: python3 get_states.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306 and
displays the states in ascending order by their ID.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Connect to MySQL server
    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
            )

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Execute the SQL query to fetch states
    cursor.execute("SELECT * FROM states ORDER BY id ASC")

    # Fetch all the rows and print them
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
