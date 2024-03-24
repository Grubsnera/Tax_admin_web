"""
Function to create the sys_user_map table and import default data.
19 December 2023 Albert van Rensburg
"""
import datetime

import pyodbc
from _my_modules import funcmariadb


def sys_user_map(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_user table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_user_map'
    success: bool = False

    # Test for a database
    if database:

        # Open the database
        db = funcmariadb.open_database()
        # Create a cursor object
        cursor = db.cursor()

        if create_table:

            # Drop table if it already exist using execute() method.
            if debug:
                print(f'Drop table {table}')
            cursor.execute(f"DROP TABLE IF EXISTS {table}")

            # Create table as per requirement
            if debug:
                print(f'Create table {table}')
            sql = f'''CREATE TABLE {table}(
            map_id int(11) AUTO_INCREMENT COMMENT 'User mapping id',
            system_id int(11) COMMENT 'Joomla user id',
            contact_id int(11) COMMENT 'Joomla contact id',
            customer_id int(11) COMMENT 'Joomla contact customer id',
            PRIMARY KEY (map_id)
            )'''
            cursor.execute(sql)

        if import_data:

            now = datetime.datetime.now()
            sql = f'''INSERT INTO {table}(
            system_id,
            contact_id,
            customer_id
            ) VALUES 
            (486, 1, 0)
            ;'''
            cursor.execute(sql)

            # Commit the changes and close the connections
            db.commit()

        # Close the database
        cursor.close()
        db.close()

        success = True

    # Return
    return success


if __name__ == '__main__':
    if sys_user_map('web_tax_admin', True, True):
        print("sys_user table created successfully")
    else:
        print("sys_user was not created successfully")
