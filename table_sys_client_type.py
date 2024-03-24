"""
Function to create the sys_client_type table and import default data.
19 December 2023 Albert van Rensburg
"""
import datetime

import pyodbc
from _my_modules import funcmariadb


def sys_client_type(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_client table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_client_type'
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
            client_type_id int(11) AUTO_INCREMENT,
            customer_id int(11),
            name varchar(50),
            description text,
            active_from date,
            active_to date,
            form_edit_id int(11),
            created_on datetime,
            created_by int(11),
            created_by_alias varchar(50),
            updated_on datetime,
            updated_by int(11),
            updated_by_alias varchar(50),
            PRIMARY KEY (client_type_id),
            UNIQUE KEY name (customer_id,name)
            )'''
            cursor.execute(sql)

        if import_data:

            now = datetime.datetime.now()
            sql = f'''INSERT INTO {table}(
            customer_id,
            name,
            description,
            active_from,
            active_to,
            form_edit_id,
            created_on,
            created_by,
            created_by_alias,
            updated_on,
            updated_by,
            updated_by_alias
            ) VALUES 
            (2, 'Individual', 'Individuals.', '2023-01-01', '2099-12-31', 6, '{now}', 0, 'Python', '{now}', 0, 'Python'),
            (2, 'Company', 'Companies and Closed Corporations.', '2023-01-01', '2099-12-31', 6, '{now}', 0, 'Python', '{now}', 0, 'Python'),
            (2, 'Trust', 'Trusts.', '2023-01-01', '2099-12-31', 6, '{now}', 0, 'Python', '{now}', 0, 'Python'),
            (2, 'Other', 'Other businesses.', '2023-01-01', '2099-12-31', 6, '{now}', 0, 'Python', '{now}', 0, 'Python')
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
    if sys_client_type('web_tax_admin', True, True):
        print("sys_client_type table created successfully")
    else:
        print("sys_client_type was not created successfully")
