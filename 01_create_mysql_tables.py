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

""" Notes NB!
This script can delete tables, and overwrite them. Be careful!
"""

""" Index
mysql_create_assi_conducted
"""

# Declare variables
l_debug: bool = True
sd_database = "Web_tax_admin"
sd_drop_table = "n"
sd_add_data = "n"
run_mysql_create_assi_conducted: bool = False
run_mysql_create_find_adequacy: bool = False
s_sql = ""  # SQL statements

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

"""
if run_mysql_create_assi_conducted:
    if l_debug:
        print("Working on the assignment conducted table...")
    mysql_create_assi_conducted.assi_conducted(s_database, s_drop_table, s_add_data)
"""


# ******************************************************************************

# Script log file
funcfile.writelog("---------------------------")
funcfile.writelog("COMPLETED: WEB_MYSQL_TABLES")
