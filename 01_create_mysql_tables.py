"""
Script to create Web mysql tables
Copyright (c) Albert Janse van Rensburg, 18 Mar 2022
"""

# Define python system objects
# import sys
# import pyodbc

# Define Functions
from _my_modules import funcfile
from _my_modules import funcmysql
import table_sys_user

""" Notes NB!
This script can delete tables, and overwrite them. Be careful!
"""

""" Index
See declare variables
"""

# Declare variables
l_debug: bool = True
sd_database = "Web_tax_admin"
sd_drop_table = "n"
sd_add_data = "n"
s_sql = ""  # SQL statements

run_sys_user: bool = False

if l_debug:
    print("WEB MYSQL INPUTS")
    print("----------------")

# Input the ia DATABASE name
print("")
print("Default:"+sd_database)
s_database = input("IA DATABASE name? ")
if s_database == "":
    s_database = sd_database

# Input the whether tables must be overwritten
print("")
print("Default:"+sd_drop_table)
s_drop_table = input("DROP Tables (y/n)? ")
if s_drop_table == "":
    s_drop_table = sd_drop_table

# Input the whether default fields should be added
print("")
print("Default:"+sd_add_data)
s_add_data = input("ADD default fields (y/n)? ")
if s_add_data == "":
    s_add_data = sd_add_data

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: WEB_MYSQL_TABLES")
funcfile.writelog("------------------------")

# Connect to the oracle database
cnxn = funcmysql.mysql_open(s_database)
curs = cnxn.cursor()
funcfile.writelog("%t OPEN DATABASE: " + s_database)

# Create the data files

if run_sys_user:
    """
    NOTE
    The system user table are populated automatically on first add.
    Therefor the s_add_data default to NO even if switch is on above.
    """
    if l_debug:
        print("Working on the sys_user table...")
    table_sys_user.sys_users(s_database, s_drop_table, "n")

# Close the database
cnxn.close()
funcfile.writelog("%t CLOSE DATABASE: " + s_database)

# ******************************************************************************

# Script log file
funcfile.writelog("---------------------------")
funcfile.writelog("COMPLETED: WEB_MYSQL_TABLES")
