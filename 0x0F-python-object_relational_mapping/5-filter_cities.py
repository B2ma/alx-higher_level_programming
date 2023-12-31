#!/usr/bin/python3
""" States Script module"""

import MySQLdb
import sys


def list_cities_warg(username, password, database_name, state_name):
    """
    Connects to a MySQL server and retrieves a list of cities
    from the specified database.

    Args:
        username (str): MySQL username.
        password (str): MySQL password.
        database_name (str): Name of the database to retrieve states from.
    Returns:
        None: Prints the cities of a given state with names matching the
        provided argument in ascending order by states.id.
    """
    try:
        connection = MySQLdb.connect(
                user=username,
                passwd=password,
                db=database_name,
                host='localhost',
                port=3306)
        cursor = connection.cursor()
        query = ("SELECT `c`.`name`FROM `cities` as `c` \
                INNER JOIN `states` AS `s` \
                ON `c`.`state_id` = `s`.`id` \
                WHERE `s`.`name` = %s\
                ORDER BY `c`.`id`")
        cursor.execute(query, (state_name,))
        cities = cursor.fetchall()
        city_names = ", ".join([city[0] for city in cities])
        print(city_names)

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
    list_cities_warg(username, password, database_name, state_name)
