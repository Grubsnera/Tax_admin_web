"""
Function to create the sys_town table and import the existing data.
23 March 2024 Albert van Rensburg
"""
import datetime
import csv
import pyodbc
from _my_modules import funcmariadb


def sys_town(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_client table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_town'
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
                town_id INT AUTO_INCREMENT,
                town_name VARCHAR(50),
                town_suburb VARCHAR(50),
                town_dialcode VARCHAR(10),
                town_postcode VARCHAR(10),
                town_coordinates VARCHAR(20),
                country_iso2 VARCHAR(2),
                form_edit_id int(11),
                created_on datetime,
                created_by int(11),
                created_by_alias varchar(50),
                updated_on datetime,
                updated_by int(11),
                updated_by_alias varchar(50),
                PRIMARY KEY (town_id),
                UNIQUE (`town_name`(50), `town_suburb`(50)),
                FOREIGN KEY (country_iso2) REFERENCES sys_country(country_iso2) ON DELETE RESTRICT ON UPDATE CASCADE
            )'''
            cursor.execute(sql)

        if import_data:

            # Read csv data previously submitted and populate SQLite table.
            count: int = 0
            with open("_external_data/postalcodes.csv", "r") as file:
                csv_reader = csv.DictReader(file)
                for row in csv_reader:
                    count += 1
                    town_name = row['town_name']
                    town_suburb = row['town_suburb']
                    town_dialcode = row['town_dialcode']
                    town_postcode = row['town_postcode']
                    town_coordinates = row['town_coordinates']
                    country_iso2 = row['country_iso2']
                    # The insert
                    sql = f'''INSERT INTO {table} (
                    town_name,
                    town_suburb,
                    town_dialcode,
                    town_postcode,
                    town_coordinates,
                    country_iso2,
                    form_edit_id,
                    created_on,
                    created_by,
                    created_by_alias,
                    updated_on,
                    updated_by,
                    updated_by_alias                
                    ) VALUES (
                    "{town_name}",
                    "{town_suburb}",
                    "{town_dialcode}",
                    "{town_postcode}",
                    "{town_coordinates}",
                    "{country_iso2}",
                    8,
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
    if sys_town('web_tax_admin', True, True):
        print("sys_town table created successfully")
    else:
        print("sys_town was not created successfully")
