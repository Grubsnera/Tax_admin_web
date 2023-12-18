"""
MariaDB functions.
15 December 2023 Albert van Rensburg
"""

import configparser
import mysql.connector
from _my_modules import funcsys


def open_database(source: str = 'web_tax_admin'):
    """
    Function to open the database.
    :param source: Source database.
    :return: Connection object.
    """

    # Variables
    debug: bool = False

    # Create a new ConfigParser object
    config = configparser.ConfigParser()
    # Read from the configuration file
    section: str = ''
    if source == 'web_tax_admin':
        section = 'WEB_TAX_ADMIN'
    config.read('.config.ini')
    if debug:
        print(config.get(section, 'server'))
        print(config.get(section, 'full_username'))
        print(config.get(section, 'full_password'))
        print(config.get(section, 'database'))

    try:
        db_connection = mysql.connector.connect(
            host=config.get(section, 'server'),
            user=config.get(section, 'full_username'),
            password=config.get(section, 'full_password'),
            database=config.get(section, 'database')
        )
        print(f"Successfully connected to {source}")
        return db_connection
    except mysql.connector.Error as error:
        print(f"Failed to connect to {source}: ".format(error))
        funcsys.ErrMessage(error)


if __name__ == '__main__':
    open_database()
