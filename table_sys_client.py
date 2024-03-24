"""
Function to create the sys_client table and import the existing data.
16 December 2023 Albert van Rensburg
"""
import datetime

import pyodbc
from _my_modules import funcmariadb


def sys_client(database: str = '', create_table: bool = False, import_data: bool = False):
    """
    Function to create the sys_client table and import the existing data.
    :param database:
    :param create_table:
    :param import_data:
    :return: bool
    """

    # Variables
    debug: bool = True
    table: str = 'sys_client'
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
                client_id INT AUTO_INCREMENT,
                customer_id INT,
                client_type INT,
                tax_number VARCHAR(10),
                name_registered VARCHAR(50),
                name_trading VARCHAR(50),
                name_surname VARCHAR(50),
                name_initials VARCHAR(10),
                name_first VARCHAR(50),
                email_address VARCHAR(50),
                email_alternate VARCHAR(50),
                address_post_1 VARCHAR(50),
                address_post_2 VARCHAR(50),
                address_post_3 VARCHAR(50),
                address_post_city VARCHAR(50),
                address_post_region VARCHAR(50),
                address_post_code VARCHAR(10),
                address_post_country VARCHAR(50),
                address_street_1 VARCHAR(50),
                address_street_2 VARCHAR(50),
                address_street_3 VARCHAR(50),
                address_street_city VARCHAR(50),
                address_street_region VARCHAR(50),
                address_street_code VARCHAR(10),
                address_street_country VARCHAR(50),
                district_magisterial VARCHAR(50),
                form_edit_id int(11),
                created_on datetime,
                created_by int(11),
                created_by_alias varchar(50),
                updated_on datetime,
                updated_by int(11),
                updated_by_alias varchar(50),
                PRIMARY KEY (client_id)
            )'''
            cursor.execute(sql)

        if import_data:

            # Connect to the Access database
            access_connection = pyodbc.connect(
                r"Driver={Microsoft Access Driver (*.mdb, *.accdb)};"
                r"DBQ=_external_data/TaxClientsData.mdb;"
            )
            access_cursor = access_connection.cursor()

            # IMPORT INDIVIDUAL DETAILS

            # Execute a query to fetch the data from the Access database
            sql = '''SELECT
                TaxNo,
                Surname,
                Initials,
                FirstNames,
                [E-mail],
                Postal1,
                Postal2,
                Postal3,
                PostalCode,
                Address1,
                Address2,
                Address3,
                AddCode,
                MagisterialDistrict
                FROM IndividualClientDetails
            '''
            access_cursor.execute(sql)

            # Insert the fetched data from Access into MySQL
            count: int = 0
            for row in access_cursor:
                count += 1
                (tax_number,
                 name_surname,
                 name_initials,
                 name_first,
                 email_address,
                 address_post_1,
                 address_post_2,
                 address_post_3,
                 address_post_code,
                 address_street_1,
                 address_street_2,
                 address_street_3,
                 address_street_code,
                 district_magisterial
                 ) = row

                # Calculated fields

                name_registered = name_surname + ' ' + name_initials

                if email_address is None:
                    email_address = ''

                if address_post_1 is None:
                    address_post_1 = ''
                else:
                    address_post_1 = address_post_1.replace(",", "").replace("'", "").replace('"', "")

                if address_post_2 is None:
                    address_post_2 = ''
                else:
                    address_post_2 = address_post_2.replace(",", "").replace("'", "").replace('"', "")

                if address_post_3 is None:
                    address_post_3 = ''
                else:
                    address_post_3 = address_post_3.replace(",", "").replace("'", "").replace('"', "")

                if address_post_code is None:
                    address_post_code = ''
                else:
                    address_post_code = address_post_code.replace(",", "").replace("'", "").replace('"', "")

                if address_street_1 is None:
                    address_street_1 = ''
                else:
                    address_street_1 = address_street_1.replace(",", "").replace("'", "").replace('"', "")

                if address_street_2 is None:
                    address_street_2 = ''
                else:
                    address_street_2 = address_street_2.replace(",", "").replace("'", "").replace('"', "")

                if address_street_3 is None:
                    address_street_3 = ''
                else:
                    address_street_3 = address_street_3.replace(",", "").replace("'", "").replace('"', "")

                if address_street_code is None:
                    address_street_code = ''
                else:
                    address_street_code = address_street_code.replace(",", "").replace("'", "").replace('"', "")

                if district_magisterial is None:
                    district_magisterial = ''

                # The insert
                sql = f'''INSERT INTO {table} (
                customer_id,
                client_type,
                tax_number,
                name_surname,
                name_initials,
                name_first,
                name_registered,
                email_address,
                address_post_1,
                address_post_2,
                address_post_3,
                address_post_code,
                address_street_1,
                address_street_2,
                address_street_3,
                address_street_code,
                district_magisterial,
                form_edit_id,
                created_on,
                created_by,
                created_by_alias,
                updated_on,
                updated_by,
                updated_by_alias                
                ) VALUES (
                1,
                1,
                "{tax_number}",
                "{name_surname}",
                "{name_initials}",
                "{name_first}",
                "{name_registered}",
                "{email_address}",
                "{address_post_1}",
                "{address_post_2}",
                "{address_post_3}",
                "{address_post_code}",
                "{address_street_1}",
                "{address_street_2}",
                "{address_street_3}",
                "{address_street_code}",
                "{district_magisterial}",
                4,
                "{now}",
                0,
                "{user}",
                "{now}",
                0,
                "{user}"
                )
                '''
                cursor.execute(sql)

            # Commit the changes and close the connections
            db.commit()

            if debug:
                print('Inserted ' + str(count) + ' individual records')

            # IMPORT COMPANY DETAILS

            # Execute a query to fetch the data from the Access database
            sql = '''SELECT
                TaxNo,
                RegisteredName,
                TradingName,
                [E-mail],
                Postal1,
                Postal2,
                PostalCode,
                RegisteredAddress1,
                RegisteredAddress2,
                RegisteredCode,
                MagisterialDistrict
                FROM CompanyCCDetails
            '''
            access_cursor.execute(sql)

            # Insert the fetched data from Access into MySQL
            count = 0
            for row in access_cursor:
                count += 1
                (tax_number,
                 name_registered,
                 name_trading,
                 email_address,
                 address_post_1,
                 address_post_2,
                 address_post_code,
                 address_street_1,
                 address_street_2,
                 address_street_code,
                 district_magisterial
                 ) = row

                # Calculated fields

                if name_trading is None:
                    name_trading = ''

                if email_address is None:
                    email_address = ''

                if address_post_1 is None:
                    address_post_1 = ''
                else:
                    address_post_1 = address_post_1.replace(",", "").replace("'", "").replace('"', "")

                if address_post_2 is None:
                    address_post_2 = ''
                else:
                    address_post_2 = address_post_2.replace(",", "").replace("'", "").replace('"', "")

                if address_post_code is None:
                    address_post_code = ''
                else:
                    address_post_code = address_post_code.replace(",", "").replace("'", "").replace('"', "")

                if address_street_1 is None:
                    address_street_1 = ''
                else:
                    address_street_1 = address_street_1.replace(",", "").replace("'", "").replace('"', "")

                if address_street_2 is None:
                    address_street_2 = ''
                else:
                    address_street_2 = address_street_2.replace(",", "").replace("'", "").replace('"', "")

                if address_street_code is None:
                    address_street_code = ''
                else:
                    address_street_code = address_street_code.replace(",", "").replace("'", "").replace('"', "")

                if district_magisterial is None:
                    district_magisterial = ''

                # The insert
                sql = f'''INSERT INTO {table} (
                customer_id,
                client_type,
                tax_number,
                name_registered,
                name_trading,
                email_address,
                address_post_1,
                address_post_2,
                address_post_code,
                address_street_1,
                address_street_2,
                address_street_code,
                district_magisterial,
                form_edit_id,
                created_on,
                created_by,
                created_by_alias,
                updated_on,
                updated_by,
                updated_by_alias                
                ) VALUES (
                1,
                2,
                "{tax_number}",
                "{name_registered}",
                "{name_trading}",
                "{email_address}",
                "{address_post_1}",
                "{address_post_2}",
                "{address_post_code}",
                "{address_street_1}",
                "{address_street_2}",
                "{address_street_code}",
                "{district_magisterial}",
                4,
                "{now}",
                0,
                "{user}",
                "{now}",
                0,
                "{user}"
                )
                '''
                cursor.execute(sql)

            # Commit the changes and close the connections
            db.commit()

            if debug:
                print('Inserted ' + str(count) + ' company records')

            # IMPORT TRUST DETAILS

            # Execute a query to fetch the data from the Access database
            sql = '''SELECT
                TaxNo,
                NameOfTrust,
                [E-mail],
                PostalAddress1,
                PostalAddress2,
                PostalCode,
                RegAdd1,
                RegAdd2,
                RegAdd3,
                RegCode,
                MagisterialDistrict
                FROM TrustClientDetails
            '''
            access_cursor.execute(sql)

            # Insert the fetched data from Access into MySQL
            count = 0
            for row in access_cursor:
                count += 1
                (tax_number,
                 name_registered,
                 email_address,
                 address_post_1,
                 address_post_2,
                 address_post_code,
                 address_street_1,
                 address_street_2,
                 address_street_3,
                 address_street_code,
                 district_magisterial
                 ) = row

                # Calculated fields

                if email_address is None:
                    email_address = ''

                if address_post_1 is None:
                    address_post_1 = ''
                else:
                    address_post_1 = address_post_1.replace(",", "").replace("'", "").replace('"', "")

                if address_post_2 is None:
                    address_post_2 = ''
                else:
                    address_post_2 = address_post_2.replace(",", "").replace("'", "").replace('"', "")

                if address_post_code is None:
                    address_post_code = ''
                else:
                    address_post_code = address_post_code.replace(",", "").replace("'", "").replace('"', "")

                if address_street_1 is None:
                    address_street_1 = ''
                else:
                    address_street_1 = address_street_1.replace(",", "").replace("'", "").replace('"', "")

                if address_street_2 is None:
                    address_street_2 = ''
                else:
                    address_street_2 = address_street_2.replace(",", "").replace("'", "").replace('"', "")

                if address_street_3 is None:
                    address_street_3 = ''
                else:
                    address_street_3 = address_street_3.replace(",", "").replace("'", "").replace('"', "")

                if address_street_code is None:
                    address_street_code = ''
                else:
                    address_street_code = address_street_code.replace(",", "").replace("'", "").replace('"', "")

                if district_magisterial is None:
                    district_magisterial = ''

                # The insert
                sql = f'''INSERT INTO {table} (
                customer_id,
                client_type,
                tax_number,
                name_registered,
                email_address,
                address_post_1,
                address_post_2,
                address_post_code,
                address_street_1,
                address_street_2,
                address_street_3,
                address_street_code,
                district_magisterial,
                form_edit_id,
                created_on,
                created_by,
                created_by_alias,
                updated_on,
                updated_by,
                updated_by_alias
                ) VALUES (
                1,
                3,
                "{tax_number}",
                "{name_registered}",
                "{email_address}",
                "{address_post_1}",
                "{address_post_2}",
                "{address_post_code}",
                "{address_street_1}",
                "{address_street_2}",
                "{address_street_3}",
                "{address_street_code}",
                "{district_magisterial}",
                4,
                "{now}",
                0,
                "{user}",
                "{now}",
                0,
                "{user}"
                )
                '''
                cursor.execute(sql)

            # Commit the changes and close the connections
            db.commit()

            if debug:
                print('Inserted ' + str(count) + ' trust records')

            # IMPORT OTHER DETAILS

            # Execute a query to fetch the data from the Access database
            sql = '''SELECT
                OBusinessNo,
                RegisteredName,
                TradingName,
                [E-mail],
                Postal1,
                Postal2,
                PostalCode,
                RegisteredAddress1,
                RegisteredAddress2,
                RegisteredCode
                FROM OtherBusinesses
            '''
            access_cursor.execute(sql)

            # Insert the fetched data from Access into MySQL
            count = 0
            for row in access_cursor:
                count += 1
                (tax_number,
                 name_registered,
                 name_trading,
                 email_address,
                 address_post_1,
                 address_post_2,
                 address_post_code,
                 address_street_1,
                 address_street_2,
                 address_street_code) = row

                # Calculated fields

                if name_trading is None:
                    name_trading = ''

                if email_address is None:
                    email_address = ''

                if address_post_1 is None:
                    address_post_1 = ''
                else:
                    address_post_1 = address_post_1.replace(",", "").replace("'", "").replace('"', "")

                if address_post_2 is None:
                    address_post_2 = ''
                else:
                    address_post_2 = address_post_2.replace(",", "").replace("'", "").replace('"', "")

                if address_post_code is None:
                    address_post_code = ''
                else:
                    address_post_code = address_post_code.replace(",", "").replace("'", "").replace('"', "")

                if address_street_1 is None:
                    address_street_1 = ''
                else:
                    address_street_1 = address_street_1.replace(",", "").replace("'", "").replace('"', "")

                if address_street_2 is None:
                    address_street_2 = ''
                else:
                    address_street_2 = address_street_2.replace(",", "").replace("'", "").replace('"', "")

                if address_street_code is None:
                    address_street_code = ''
                else:
                    address_street_code = address_street_code.replace(",", "").replace("'", "").replace('"', "")

                # The insert
                sql = f'''INSERT INTO {table} (
                customer_id,
                client_type,
                tax_number,
                name_registered,
                name_trading,
                email_address,
                address_post_1,
                address_post_2,
                address_post_code,
                address_street_1,
                address_street_2,
                address_street_code,
                form_edit_id,
                created_on,
                created_by,
                created_by_alias,
                updated_on,
                updated_by,
                updated_by_alias
                ) VALUES (
                1,
                4,
                "{tax_number}",
                "{name_registered}",
                "{name_trading}",
                "{email_address}",
                "{address_post_1}",
                "{address_post_2}",
                "{address_post_code}",
                "{address_street_1}",
                "{address_street_2}",
                "{address_street_code}",
                4,
                "{now}",
                0,
                "{user}",
                "{now}",
                0,
                "{user}"
                )
                '''
                cursor.execute(sql)

            # Commit the changes and close the connections
            db.commit()

            if debug:
                print('Inserted ' + str(count) + ' other business records')

            # Close the access database
            access_cursor.close()
            access_connection.close()

        # Close the database
        cursor.close()
        db.close()

        success = True

    # Return
    return success


if __name__ == '__main__':
    if sys_client('web_tax_admin', True, True):
        print("sys_client table created successfully")
    else:
        print("sys_client was not created successfully")
