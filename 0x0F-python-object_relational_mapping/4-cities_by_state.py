#!/usr/bin/python3
""" States Script module"""

import MySQLdb
import sys


def list_cities(username, password, database_name):
    """
    Connects to a MySQL server and retrieves a list of cities
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database to retrieve states from.
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
        query = ("SELECT `c`.`id`, `c`.`name`, `s`.`name`\
                FROM `cities` as c\
                INNER JOIN `states` as `s` \
                ON `c`.`state_id` = `s`.`id` \
                ORDER BY `c`.`id`")
        cursor.execute(query)
        cities = cursor.fetchall()
        for city in cities:
            print(city)

    except MySQLdb.Error as e:
        print("Error connecting to the database:", e)
    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[1]
    database_name = sys.argv[3]
    list_cities(username, password, database_name)
