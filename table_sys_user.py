"""
Function to create the sys_user table and import default data.
19 December 2023 Albert van Rensburg
"""
import datetime

import pyodbc
from _my_modules import funcmariadb


def sys_user(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_user table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_user'
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
            user_id int(11) AUTO_INCREMENT COMMENT 'User id',
            system_id int(11) COMMENT 'Joomla user id',
            active_to date,
            form_edit_id int(11),
            created_on datetime,
            created_by int(11),
            created_by_alias varchar(50),
            updated_on datetime,
            updated_by int(11),
            updated_by_alias varchar(50),
            PRIMARY KEY (user_id)
            )'''
            cursor.execute(sql)

        if import_data:

            now = datetime.datetime.now()
            sql = f'''INSERT INTO {table}(
            system_id,
            active_to,
            form_edit_id,
            created_on,
            created_by,
            created_by_alias,
            updated_on,
            updated_by,
            updated_by_alias            
            ) VALUES 
            (486, '2099-12-31', 5, '{now}', 0, 'Python', '{now}', 0, 'Python')
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
    if sys_user('web_tax_admin', True, True):
        print("sys_user table created successfully")
    else:
        print("sys_user was not created successfully")
