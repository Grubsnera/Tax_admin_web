"""
Script to create Web mysql tables
Copyright (c) Albert Janse van Rensburg, 18 Mar 2022
"""

# Define python system objects
# import sys
# import pyodbc

# Define Functions
from _my_modules import funcfile
from _my_modules import funcmariadb
import table_sys_user
import table_sys_user_map
import table_sys_client
import table_sys_client_type
import table_sys_country
import table_sys_town

""" Notes NB!
This script can delete tables, and overwrite them. Be careful!
"""

""" Index
See declare variables
"""

# Declare variables
debug: bool = True
database = "web_tax_joomla"

run_sys_user: bool = False
run_sys_user_map: bool = False
run_sys_client_type: bool = False
run_sys_client: bool = True
run_sys_country: bool = False
run_sys_town: bool = False

if debug:
    print("WEB MYSQL INPUTS")
    print("----------------")

# Script log file
funcfile.writelog("Now")
funcfile.writelog("SCRIPT: WEB_MYSQL_TABLES")
funcfile.writelog("------------------------")

# Create the data files

if run_sys_user:
    if debug:
        print("Build and import users")
    if table_sys_user.sys_user(database, True, True):
        print("sys_user table created successfully")
    else:
        print("sys_user was not created successfully")

if run_sys_user_map:
    if debug:
        print("Build and import users")
    if table_sys_user_map.sys_user_map(database, True, True):
        print("sys_user_map table created successfully")
    else:
        print("sys_user_map was not created successfully")

if run_sys_client_type:
    if debug:
        print("Build and import client types")
    if table_sys_client_type.sys_client_type(database, True, True):
        print("sys_client table created successfully")
    else:
        print("sys_client was not created successfully")

if run_sys_client:
    if debug:
        print("Build and import clients")
    if table_sys_client.sys_client(database, True, True):
        print("sys_client table created successfully")
    else:
        print("sys_client was not created successfully")

if run_sys_country:
    if debug:
        print("Build and import countries")
    if table_sys_country.sys_country(database, True, True):
        print("sys_country table created successfully")
    else:
        print("sys_country was not created successfully")

if run_sys_town:
    if debug:
        print("Build and import towns")
    if table_sys_town.sys_town(database, True, True):
        print("sys_town table created successfully")
    else:
        print("sys_town was not created successfully")

# ******************************************************************************

# Script log file
funcfile.writelog("---------------------------")
funcfile.writelog("COMPLETED: WEB_MYSQL_TABLES")
