"""
Copyright (c) Albert B Janse van Rensburg, 15 Mar 2022
"""

# Define python system objects
import csv
import hashlib
# import sys
# import pyodbc

# Define Functions
from _my_modules import funcmysql
from _my_modules import funcfile

"""  Index - list of tables created
SYS_TOWNS (Table to add and edit towns.)
"""


def sys_towns(s_database: str = "", s_drop_table: str = "", s_add_data: str = "", s_edit: str = "", s_delete: str = ""):
    """
    Script to build SYSTEM TOWNS table with contents
    :param s_database: Database in which to create the table
    :param s_drop_table: Should table be dropped? (y/n)
    :param s_add_data: Should default data be added? (y/n)
    :param s_edit: Default edit form id?
    :param s_delete: Default delete form id?
    :return: Nothing
    """

    # Declare variables
    l_debug: bool = False
    sd_database: str = "Web_tax_joomla"
    sd_drop_table: str = "n"
    sd_add_data: str = "n"
    sd_edit = "7"
    sd_delete = "8"
    ed_path = "_external_data/"  # external data path
    s_table: str = "sys_towns"

    if l_debug:
        print("WEB TABLE INPUTS")
        print("----------------")

    # Input the ia DATABASE name
    if l_debug or s_database == "":
        print("")
        print("Default:" + sd_database)
    if s_database == "": 
        s_database = input("IA DATABASE name? ")
    if s_database == "":
        s_database = sd_database

    # Input the whether tables must be overwritten
    if l_debug or s_drop_table == "":
        print("")
        print("Default:" + sd_drop_table)
    if s_drop_table == "":
        s_drop_table = input("DROP Table (y/n)? ")
    if s_drop_table == "":
        s_drop_table = sd_drop_table

    # Input the whether default fields should be added
    if l_debug or s_add_data == "":
        print("")
        print("Default:" + sd_add_data)
    if s_add_data == "":
        s_add_data = input("ADD default fields (y/n)? ")
    if s_add_data == "":
        s_add_data = sd_add_data

    # Input the edit form id
    if l_debug or s_edit == "":
        print("")
        print("Default:" + sd_edit)
    if s_edit == "":
        s_edit = input("Edit form id? ")
    if s_edit == "":
        s_edit = sd_edit

    # Input the delete form id
    if l_debug or s_delete == "":
        print("")
        print("Default:" + sd_delete)
    if s_delete == "":
        s_delete = input("Delete form id? ")
    if s_delete == "":
        s_delete = sd_delete

    # Script log file
    funcfile.writelog("Now")
    funcfile.writelog("SCRIPT: WEB_SYSTEM_TOWNS")
    funcfile.writelog("----------------------------")

    # Connect to the oracle database
    cnxn = funcmysql.mysql_open(s_database)
    curs = cnxn.cursor()
    funcfile.writelog("%t OPEN DATABASE: " + s_database)

    # Create SYS_TOWNS table ***************************************************
    if s_drop_table == "y":
        curs.execute("DROP TABLE IF EXISTS " + s_table)
        funcfile.writelog("%t DROPPED TABLE: SYS_TOWNS(" + s_table + ")")
    s_sql: str = """
    CREATE TABLE IF NOT EXISTS `%TABLE%` (
    `town_id` int(11) NOT NULL AUTO_INCREMENT,
    `town_name` varchar(100) NOT NULL,
    `town_suburb` varchar(100) NOT NULL,
    `town_dial` varchar(10) NOT NULL,
    `town_post` varchar(10) NOT NULL,
    `town_coordinates` varchar(255) NOT NULL,
    `town_coun_iso2` varchar(2) NOT NULL,
    `town_form_edit` int(4) NOT NULL,
    `town_form_delete` int(4) NOT NULL,
    `town_hash` varchar(32) NOT NULL,
    `town_actions` varchar(1095) NOT NULL,    
    `created` datetime,
    `created_by` int(11),
    `created_by_alias` varchar(100),
    `modified` datetime,
    `modified_by` int(11),
    `modified_by_alias` varchar(100),
    PRIMARY KEY (`town_id`),
    UNIQUE KEY `TOWN-SUBURB` (`town_name`,`town_suburb`)
    )
    ENGINE = InnoDB
    CHARSET=utf8mb4
    COLLATE utf8mb4_unicode_ci
    COMMENT = 'Table to store town details.'
    """ + ";"
    s_sql = s_sql.replace("%TABLE%", s_table)
    curs.execute(s_sql)
    funcfile.writelog("%t CREATED TABLE: SYS_TOWNS(" + s_table + ")")

    # Insert SYS_TOWNS data
    if s_add_data == "y":

        co = open(ed_path + "postalcodes.csv", newline=None)
        co_reader = csv.reader(co)
        for row in co_reader:
            if row[0] == "town_name":
                continue
            else:
                s_sql = """
                INSERT INTO `%TABLE%` (
                `town_name`,
                `town_suburb`,
                `town_dial`,
                `town_post`,
                `town_coordinates`,
                `town_coun_iso2`,
                `town_form_edit`,
                `town_form_delete`,
                `town_hash`,
                `town_actions`,
                `created`,
                `created_by_alias`
                )
                VALUES
                (
                """ + \
                    "'" + row[0] + \
                    "','" + row[1] + \
                    "','" + row[2] + \
                    "','" + row[3] + \
                    "','" + row[4] + \
                    "','" + row[5] + \
                    "','%EDIT%" + \
                    "','%DELETE%" + \
                    "','%HASH%" + \
                    "','%ACTIONS%" + \
                    "', NOW()" + \
                    ",'python'" + \
                    ");"

                s_sql = s_sql.replace("%TABLE%", s_table)
                s_sql = s_sql.replace("%EDIT%", s_edit)
                s_sql = s_sql.replace("%DELETE%", s_delete)
                s_hash_value: str = row[0] + row[1]
                s_hash: str = hashlib.md5(s_hash_value.encode('utf-8')).hexdigest()
                s_sql = s_sql.replace("%HASH%", s_hash)
                s_actions: str = '<a href = "https://www.tax-admin.co.za/index.php?option=com_rsform&formId='
                s_actions += s_edit
                s_actions += '&hash='
                s_actions += s_hash
                s_actions += '">Edit</a> | '
                s_actions += '<a href = "https://www.tax-admin.co.za/index.php?option=com_rsform&formId='
                s_actions += s_delete
                s_actions += '&hash='
                s_actions += s_hash
                s_actions += '">Delete</a>'
                s_sql = s_sql.replace("%ACTIONS%", s_actions)
                curs.execute(s_sql)

        # Close the imported data file
        co.close()
        cnxn.commit()
        funcfile.writelog("%t INSERTED DATA: SYS_TOWNS(" + s_table + ")")

    # ******************************************************************************

    # Script log file
    funcfile.writelog("-------------------------------")
    funcfile.writelog("COMPLETED: WEB_SYSTEM_TOWNS")

    return


if __name__ == '__main__':
    try:
        sys_towns()
        # Test automated function - delete and create new table with data
        # sys_users("Web_tax_admin", "y", "y", "7", "8")
    finally:
        print("")
