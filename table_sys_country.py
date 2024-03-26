"""
Function to create the sys_country table and import the existing data.
23 March 2024 Albert van Rensburg
"""
import datetime
import csv
import pyodbc
from _my_modules import funcmariadb


def sys_country(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_client table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_country'
    user: str = 'Python'
    now: str = datetime.datetime.now()
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
                country_id INT AUTO_INCREMENT,
                country_name VARCHAR(50),
                country_iso2 VARCHAR(2),
                country_iso3 VARCHAR(3),
                country_ison VARCHAR(3),
                country_dialcode VARCHAR(10),
                country_timezone VARCHAR(10),
                form_edit_id int(11),
                created_on datetime,
                created_by int(11),
                created_by_alias varchar(50),
                updated_on datetime,
                updated_by int(11),
                updated_by_alias varchar(50),
                PRIMARY KEY (country_id),
                UNIQUE (country_iso2),
                UNIQUE (country_iso3),
                UNIQUE (country_ison)
            )'''
            cursor.execute(sql)

        if import_data:

            # Read csv data previously submitted and populate SQLite table.
            count: int = 0
            with open("_external_data/countries.csv", "r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    count += 1
                    country_name = row['country_name']
                    country_iso2 = row['country_iso2']
                    country_iso3 = row['country_iso3']
                    country_ison = row['country_ison']
                    country_dialcode = row['country_dialcode']
                    country_timezone = row['country_timezone']
                    # The insert
                    sql = f'''INSERT INTO {table} (
                    country_name,
                    country_iso2,
                    country_iso3,
                    country_ison,
                    country_dialcode,
                    country_timezone,
                    form_edit_id,
                    created_on,
                    created_by,
                    created_by_alias,
                    updated_on,
                    updated_by,
                    updated_by_alias                
                    ) VALUES (
                    "{country_name}",
                    "{country_iso2}",
                    "{country_iso3}",
                    "{country_ison}",
                    "{country_dialcode}",
                    "{country_timezone}",
                    7,
                    "{now}",
                    0,
                    "{user}",
                    "{now}",
                    0,
                    "{user}"
                    )
                    '''
                    cursor.execute(sql)
            db.commit()

            if debug:
                print('Inserted ' + str(count) + ' individual records')

            # Close the access database

        # Close the database
        cursor.close()
        db.close()

        success = True

    # Return
    return success


if __name__ == '__main__':
    if sys_country('web_tax_admin', True, True):
        print("sys_country table created successfully")
    else:
        print("sys_country was not created successfully")
