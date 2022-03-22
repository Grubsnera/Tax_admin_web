"""
Copyright (c) Albert B Janse van Rensburg, 15 Mar 2022
"""

# Define python system objects
# import sys
# import pyodbc

# Define Functions
from _my_modules import funcmysql
from _my_modules import funcfile

"""  Index - list of tables created
SYS_USERS (Table to store and replicate system users.)
"""


def sys_users(s_database: str = "", s_drop_table: str = "", s_add_data: str = ""):
    """
    Script to build SYSTEM USERS table with contents
    :param s_database: Database in which to create the table
    :param s_drop_table: Should table be dropped? (y/n)
    :param s_add_data: Should default data be added? (y/n)
    :return: Nothing
    """

    # Declare variables
    l_debug: bool = False
    sd_database: str = "Web_tax_admin"
    sd_drop_table: str = "n"
    sd_add_data: str = "n"
    s_table: str = "sys_users"

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

    # Script log file
    funcfile.writelog("Now")
    funcfile.writelog("SCRIPT: WEB_SYSTEM_USERS")
    funcfile.writelog("------------------------")

    # Connect to the oracle database
    cnxn = funcmysql.mysql_open(s_database)
    curs = cnxn.cursor()
    funcfile.writelog("%t OPEN DATABASE: " + s_database)

    # Create SYS_USERS table ***************************************************
    if s_drop_table == "y":
        curs.execute("DROP TABLE IF EXISTS " + s_table)
        funcfile.writelog("%t DROPPED TABLE: SYS_USERS(" + s_table + ")")
    s_sql: str = """
    CREATE TABLE IF NOT EXISTS `%TABLE%` (
    `id` int(11) NOT NULL,
    `user_id` int(11) NOT NULL,
    `name` varchar(400) NOT NULL,
    `username` varchar(150) NOT NULL,
    `password` varchar(100) NOT NULL,
    `email` varchar(100) NOT NULL,
    `block` tinyint(4) NOT NULL DEFAULT 0,
    `reset` tinyint(4) NOT NULL DEFAULT 0,
    `user_group` int(10) UNSIGNED NOT NULL,
    `created` datetime,
    `created_by` int(11),
    `created_by_alias` varchar(100),
    `modified` datetime,
    `modified_by` int(11),
    `modified_by_alias` varchar(100),
    PRIMARY KEY (`id`),
    INDEX `fb_groupby_user_group_INDEX` (`user_group`)    
    )
    ENGINE = InnoDB
    CHARSET=utf8mb4
    COLLATE utf8mb4_unicode_ci
    COMMENT = 'Table to store and replicate system users.'
    """ + ";"
    s_sql = s_sql.replace("%TABLE%", s_table)
    curs.execute(s_sql)
    funcfile.writelog("%t CREATED TABLE: SYS_USERS(" + s_table + ")")

    # Insert SYS_USERS data
    if s_add_data == "y":
        s_sql = """
        INSERT INTO `%TABLE%` (
        `id`,
        `user_id`,
        `name`,
        `username`,
        `password`,
        `email`,
        `block`,
        `reset`,
        `user_group`,
        `created`,
        `created_by_alias`
        )
        VALUES
        (928, 928, 'WebMaster', 'webmaster', '', 'webmaster@tax-admin.co.za', 0, 0, 8, NOW(), 'Python'),
        (914, 914, 'Albert van Rensburg', 'albertjvr', '', 'albertjvr@outlook.com', 0, 0, 8, NOW(), 'Python')
        """ + ";"
        s_sql = s_sql.replace("%TABLE%", s_table)
        curs.execute(s_sql)
        cnxn.commit()
        funcfile.writelog("%t INSERTED DATA: SYS_USERS(" + s_table + ")")

    # ******************************************************************************

    # Script log file
    funcfile.writelog("---------------------------")
    funcfile.writelog("COMPLETED: WEB_SYSTEM_USERS")

    return


if __name__ == '__main__':
    try:
        sys_users()
        # Test automated function - delete and create new table with data
        # sys_users("Web_tax_admin", "y", "y")
    finally:
        print("")
