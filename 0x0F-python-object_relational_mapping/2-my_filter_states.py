#!/usr/bin/python3
"""
Module: 2-my_filter_states
Description: Retrieves and displays all matching states from the states table
             in the hbtn_0e_0_usa database.
Usage:     ./2-my_filter_states.py <mysql_username> \
                                <mysql_password> \
                                <database_name> \
                                <state_name_searched>
"""
import sys
import MySQLdb

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(
        user=username,
        port=3306,
        host="localhost",
        passwd=password,
        db=database
    )
    cursor = db.cursor()

    query = """
        SELECT *
        FROM states
        WHERE name LIKE '{:s}'
        ORDER BY id ASC
    """.format(state_name)

    cursor.execute(query)
    matching_states = cursor.fetchall()

    for state in matching_states:
        if state[1] == state_name:
            print(state)

    cursor.close()
    db.close()
