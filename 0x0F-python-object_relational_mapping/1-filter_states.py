#!/usr/bin/env python3
"""
This script lists all states with a name starting with `N`
from the database `hbtn_0e_0_usa`.
"""

import sys
import MySQLdb


if __name__ == "__main__":
    """
    Check if all required arguments are provided
    """
    if len(sys.argv) != 4:
        print("Usage: python3 list_states.py <username> <password> <database>")
        sys.exit(1)

    # Retrieve command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        """
        Connect to MySQL server
        """
        connection = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database
        )

        # Create a cursor object to execute queries
        cursor = connection.cursor()

        # Execute the query to retrieve states starting with N
        cursor.execute("SELECT DISTINCT * FROM states "
                       "WHERE name LIKE 'N%' "
                       "ORDER BY id ASC")

        # Fetch all rows from the result set
        rows = cursor.fetchall()

        # Keep track of unique state names
        unique_states = set()

        # Print the unique results
        for row in rows:
            state_id, state_name = row
            if state_name not in unique_states:
                unique_states.add(state_name)
                print(row)

    except MySQLdb.Error as e:
        print(f"Error connecting to MySQL server: {e}")
        sys.exit(1)

    finally:
        # Close the database connection
        if connection:
            connection.close()
