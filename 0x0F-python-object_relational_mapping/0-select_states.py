#!/usr/bin/env python3
"""
This script retrieves all states from the hbtn_0e_0_usa database.

Usage: python3 get_states.py <mysql_username> <mysql_password> <database_name>

The script connects to a MySQL server running on localhost at port 3306 and
displays the states in ascending order by their ID.
"""

import MySQLdb
import sys


if __name__ == "__main__":
    """
    Get MySQL credentials from command-line arguments.
    """
    mysql_user = sys.argv[1]
    mysql_password = sys.argv[2]
    database_name = sys.argv[3]

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

    # Print the states in the desired format.
    for row in rows:
        print(row)

    # Close the cursor and database connection
    cursor.close()
    db.close()
