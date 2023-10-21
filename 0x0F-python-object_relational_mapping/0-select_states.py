#!/usr/bin/python3
""" States Script module"""

import MySQLdb
import sys


def list_states(username, password, database_name):
    """
    Connects to a MySQL server and retrieves a list of states
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database to retrieve states from.
    Returns:
        None: Prints the list of states sorted by states.id in ascending order.
    """
    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database_name,
                host='localhost',
                port=3306)
        cursor = connection.cursor()
        query = "SELECT * FROM states ORDER BY states.id ASC"
        cursor.execute(query)
        states = cursor.fetchall()
        for state in states:
            print(state)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[1]
    database_name = sys.argv[3]
    list_states(username, password, database_name)
