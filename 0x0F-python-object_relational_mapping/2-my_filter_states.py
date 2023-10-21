#!/usr/bin/python3
""" States Script module"""

import MySQLdb
import sys


def list_states_inputed(username, password, database_name, state_name):
    """
    Connects to a MySQL server and retrieves a list of states
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database to retrieve states from.
        state_name (str): State name to search for in the database.
    Returns:
        None: Prints the states with names matching the provided
        argument in ascending order by states.id.
    """
    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database_name,
                host='localhost',
                port=3306)
        cursor = connection.cursor()
        query = """
                SELECT s.id, s.name
                FROM states AS s
                INNER JOIN (
                    SELECT DISTINCT name, MIN(id) AS id
                    FROM states
                    WHERE name = '{}'
                    GROUP BY name
                ) AS subquery
                ON s.id = subquery.id
                ORDER BY s.id ASC
                """.format(state_name)
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
    state_name = sys.argv[4]
    list_states_inputed(username, password, database_name, state_name)
