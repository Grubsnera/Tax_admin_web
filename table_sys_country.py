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
SYS_COUNTRIES (Table to store and replicate system users.)
"""


def sys_countries(s_database: str = "", s_drop_table: str = "", s_add_data: str = ""):
    """
    Script to build SYSTEM COUNTRIES table with contents
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
    s_table: str = "sys_countries"

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
    funcfile.writelog("SCRIPT: WEB_SYSTEM_COUNTRIES")
    funcfile.writelog("----------------------------")

    # Connect to the oracle database
    cnxn = funcmysql.mysql_open(s_database)
    curs = cnxn.cursor()
    funcfile.writelog("%t OPEN DATABASE: " + s_database)

    # Create SYS_COUNTRIES table ***************************************************
    if s_drop_table == "y":
        curs.execute("DROP TABLE IF EXISTS " + s_table)
        funcfile.writelog("%t DROPPED TABLE: SYS_COUNTRIES(" + s_table + ")")
    s_sql: str = """
    CREATE TABLE IF NOT EXISTS `%TABLE%` (
    `coun_id` int(11) NOT NULL,
    `coun_name` varchar(100) DEFAULT NULL,
    `coun_iso2` varchar(2) NOT NULL,
    `coun_iso3` varchar(3) DEFAULT NULL,
    `coun_ison` varchar(3) DEFAULT NULL,
    `created` datetime,
    `created_by` int(11),
    `created_by_alias` varchar(100),
    `modified` datetime,
    `modified_by` int(11),
    `modified_by_alias` varchar(100),
    PRIMARY KEY (`coun_id`)
    )
    ENGINE = InnoDB
    CHARSET=utf8mb4
    COLLATE utf8mb4_unicode_ci
    COMMENT = 'Table to store and replicate system users.'
    """ + ";"
    s_sql = s_sql.replace("%TABLE%", s_table)
    curs.execute(s_sql)
    funcfile.writelog("%t CREATED TABLE: SYS_COUNTRIES(" + s_table + ")")
    cnxn.commit()

    # Insert SYS_COUNTRIES data
    if s_add_data == "y":
        s_sql = """
        INSERT INTO `%TABLE%` (
        `coun_id`,
        `coun_name`,
        `coun_iso2`,
        `coun_iso3`,
        `coun_ison`,
        `created`,
        `created_by_alias`
        )
        VALUES
        (1, "SOUTH AFRICA", "ZA", "ZAF", "710", NOW(), "Python"),
        (2, "ALAND ISLANDS", "AX", "ALA", "248", NOW(), "Python"),
        (3, "ALBANIA", "AL", "ALB", "8", NOW(), "Python"),
        (4, "ALGERIA", "DZ", "DZA", "12", NOW(), "Python"),
        (5, "AMERICAN SAMOA", "AS", "ASM", "16", NOW(), "Python"),
        (6, "ANDORRA", "AD", "AND", "20", NOW(), "Python"),
        (7, "ANGOLA", "AO", "AGO", "24", NOW(), "Python"),
        (8, "ANGUILLA", "AI", "AIA", "660", NOW(), "Python"),
        (9, "ANTARCTICA", "AQ", "ATA", "10", NOW(), "Python"),
        (10, "ANTIGUA AND BARBUDA", "AG", "ATG", "28", NOW(), "Python"),
        (11, "ARGENTINA", "AR", "ARG", "32", NOW(), "Python"),
        (12, "ARMENIA", "AM", "ARM", "51", NOW(), "Python"),
        (13, "ARUBA", "AW", "ABW", "533", NOW(), "Python"),
        (14, "AUSTRALIA", "AU", "AUS", "36", NOW(), "Python"),
        (15, "AUSTRIA", "AT", "AUT", "40", NOW(), "Python"),
        (16, "AZERBAIJAN", "AZ", "AZE", "31", NOW(), "Python"),
        (17, "BAHAMAS", "BS", "BHS", "44", NOW(), "Python"),
        (18, "BAHRAIN", "BH", "BHR", "48", NOW(), "Python"),
        (19, "BANGLADESH", "BD", "BGD", "50", NOW(), "Python"),
        (20, "BARBADOS", "BB", "BRB", "52", NOW(), "Python"),
        (21, "BELARUS", "BY", "BLR", "112", NOW(), "Python"),
        (22, "BELGIUM", "BE", "BEL", "56", NOW(), "Python"),
        (23, "BELIZE", "BZ", "BLZ", "84", NOW(), "Python"),
        (24, "BENIN", "BJ", "BEN", "204", NOW(), "Python"),
        (25, "BERMUDA", "BM", "BMU", "60", NOW(), "Python"),
        (26, "BHUTAN", "BT", "BTN", "64", NOW(), "Python"),
        (27, "BOLIVIA PLURINATIONAL STATE OF", "BO", "BOL", "68", NOW(), "Python"),
        (28, "BONAIRE, SINT EUSTATIUS AND SABA", "BQ", "BES", "535", NOW(), "Python"),
        (29, "BOSNIA AND HERZEGOVINA", "BA", "BIH", "70", NOW(), "Python"),
        (30, "BOTSWANA", "BW", "BWA", "72", NOW(), "Python"),
        (31, "BOUVET ISLAND", "BV", "BVT", "74", NOW(), "Python"),
        (32, "BRAZIL", "BR", "BRA", "76", NOW(), "Python"),
        (33, "BRITISH INDIAN OCEAN TERRITORY", "IO", "IOT", "86", NOW(), "Python"),
        (34, "BRUNEI DARUSSALAM", "BN", "BRN", "96", NOW(), "Python"),
        (35, "BULGARIA", "BG", "BGR", "100", NOW(), "Python"),
        (36, "BURKINA FASO", "BF", "BFA", "854", NOW(), "Python"),
        (37, "BURUNDI", "BI", "BDI", "108", NOW(), "Python"),
        (38, "CABO VERDE", "CV", "CPV", "132", NOW(), "Python"),
        (39, "CAMBODIA", "KH", "KHM", "116", NOW(), "Python"),
        (40, "CAMEROON", "CM", "CMR", "120", NOW(), "Python"),
        (41, "CANADA", "CA", "CAN", "124", NOW(), "Python"),
        (42, "CAYMAN ISLANDS", "KY", "CYM", "136", NOW(), "Python"),
        (43, "CENTRAL AFRICAN REPUBLIC", "CF", "CAF", "140", NOW(), "Python"),
        (44, "CHAD", "TD", "TCD", "148", NOW(), "Python"),
        (45, "CHILE", "CL", "CHL", "152", NOW(), "Python"),
        (46, "CHINA", "CN", "CHN", "156", NOW(), "Python"),
        (47, "CHRISTMAS ISLAND", "CX", "CXR", "162", NOW(), "Python"),
        (48, "COCOS KEELING ISLANDS", "CC", "CCK", "166", NOW(), "Python"),
        (49, "COLOMBIA", "CO", "COL", "170", NOW(), "Python"),
        (50, "COMOROS", "KM", "COM", "174", NOW(), "Python"),
        (51, "CONGO", "CG", "COG", "178", NOW(), "Python"),
        (52, "CONGO DEMOCRATIC REPUBLIC OF THE", "CD", "COD", "180", NOW(), "Python"),
        (53, "COOK ISLANDS", "CK", "COK", "184", NOW(), "Python"),
        (54, "COSTA RICA", "CR", "CRI", "188", NOW(), "Python"),
        (55, "COTE DIVOIRE", "CI", "CIV", "384", NOW(), "Python"),
        (56, "CROATIA", "HR", "HRV", "191", NOW(), "Python"),
        (57, "CUBA", "CU", "CUB", "192", NOW(), "Python"),
        (58, "CURACAO", "CW", "CUW", "531", NOW(), "Python"),
        (59, "CYPRUS", "CY", "CYP", "196", NOW(), "Python"),
        (60, "CZECH REPUBLIC", "CZ", "CZE", "203", NOW(), "Python"),
        (61, "DENMARK", "DK", "DNK", "208", NOW(), "Python"),
        (62, "DJIBOUTI", "DJ", "DJI", "262", NOW(), "Python"),
        (63, "DOMINICA", "DM", "DMA", "212", NOW(), "Python"),
        (64, "DOMINICAN REPUBLIC", "DO", "DOM", "214", NOW(), "Python"),
        (65, "ECUADOR", "EC", "ECU", "218", NOW(), "Python"),
        (66, "EGYPT", "EG", "EGY", "818", NOW(), "Python"),
        (67, "EL SALVADOR", "SV", "SLV", "222", NOW(), "Python"),
        (68, "EQUATORIAL GUINEA", "GQ", "GNQ", "226", NOW(), "Python"),
        (69, "ERITREA", "ER", "ERI", "232", NOW(), "Python"),
        (70, "ESTONIA", "EE", "EST", "233", NOW(), "Python"),
        (71, "ETHIOPIA", "ET", "ETH", "231", NOW(), "Python"),
        (72, "FALKLAND ISLANDS MALVINAS", "FK", "FLK", "238", NOW(), "Python"),
        (73, "FAROE ISLANDS", "FO", "FRO", "234", NOW(), "Python"),
        (74, "FIJI", "FJ", "FJI", "242", NOW(), "Python"),
        (75, "FINLAND", "FI", "FIN", "246", NOW(), "Python"),
        (76, "FRANCE", "FR", "FRA", "250", NOW(), "Python"),
        (77, "FRENCH GUIANA", "GF", "GUF", "254", NOW(), "Python"),
        (78, "FRENCH POLYNESIA", "PF", "PYF", "258", NOW(), "Python"),
        (79, "FRENCH SOUTHERN TERRITORIES", "TF", "ATF", "260", NOW(), "Python"),
        (80, "GABON", "GA", "GAB", "266", NOW(), "Python"),
        (81, "GAMBIA", "GM", "GMB", "270", NOW(), "Python"),
        (82, "GEORGIA", "GE", "GEO", "268", NOW(), "Python"),
        (83, "GERMANY", "DE", "DEU", "276", NOW(), "Python"),
        (84, "GHANA", "GH", "GHA", "288", NOW(), "Python"),
        (85, "GIBRALTAR", "GI", "GIB", "292", NOW(), "Python"),
        (86, "GREECE", "GR", "GRC", "300", NOW(), "Python"),
        (87, "GREENLAND", "GL", "GRL", "304", NOW(), "Python"),
        (88, "GRENADA", "GD", "GRD", "308", NOW(), "Python"),
        (89, "GUADELOUPE", "GP", "GLP", "312", NOW(), "Python"),
        (90, "GUAM", "GU", "GUM", "316", NOW(), "Python"),
        (91, "GUATEMALA", "GT", "GTM", "320", NOW(), "Python"),
        (92, "GUERNSEY", "GG", "GGY", "831", NOW(), "Python"),
        (93, "GUINEA", "GN", "GIN", "324", NOW(), "Python"),
        (94, "GUINEA-BISSAU", "GW", "GNB", "624", NOW(), "Python"),
        (95, "GUYANA", "GY", "GUY", "328", NOW(), "Python"),
        (96, "HAITI", "HT", "HTI", "332", NOW(), "Python"),
        (97, "HEARD ISLAND AND MCDONALD ISLANDS", "HM", "HMD", "334", NOW(), "Python"),
        (98, "HOLY SEE", "VA", "VAT", "336", NOW(), "Python"),
        (99, "HONDURAS", "HN", "HND", "340", NOW(), "Python"),
        (100, "HONG KONG", "HK", "HKG", "344", NOW(), "Python"),
        (101, "HUNGARY", "HU", "HUN", "348", NOW(), "Python"),
        (102, "ICELAND", "IS", "ISL", "352", NOW(), "Python"),
        (103, "INDIA", "IN", "IND", "356", NOW(), "Python"),
        (104, "INDONESIA", "ID", "IDN", "360", NOW(), "Python"),
        (105, "IRAN ISLAMIC REPUBLIC OF", "IR", "IRN", "364", NOW(), "Python"),
        (106, "IRAQ", "IQ", "IRQ", "368", NOW(), "Python"),
        (107, "IRELAND", "IE", "IRL", "372", NOW(), "Python"),
        (108, "ISLE OF MAN", "IM", "IMN", "833", NOW(), "Python"),
        (109, "ISRAEL", "IL", "ISR", "376", NOW(), "Python"),
        (110, "ITALY", "IT", "ITA", "380", NOW(), "Python"),
        (111, "JAMAICA", "JM", "JAM", "388", NOW(), "Python"),
        (112, "JAPAN", "JP", "JPN", "392", NOW(), "Python"),
        (113, "JERSEY", "JE", "JEY", "832", NOW(), "Python"),
        (114, "JORDAN", "JO", "JOR", "400", NOW(), "Python"),
        (115, "KAZAKHSTAN", "KZ", "KAZ", "398", NOW(), "Python"),
        (116, "KENYA", "KE", "KEN", "404", NOW(), "Python"),
        (117, "KIRIBATI", "KI", "KIR", "296", NOW(), "Python"),
        (118, "KOREA DEMOCRATIC PEOPLES REPUBLIC OF", "KP", "PRK", "408", NOW(), "Python"),
        (119, "KOREA REPUBLIC OF", "KR", "KOR", "410", NOW(), "Python"),
        (120, "KUWAIT", "KW", "KWT", "414", NOW(), "Python"),
        (121, "KYRGYZSTAN", "KG", "KGZ", "417", NOW(), "Python"),
        (122, "LAO PEOPLES DEMOCRATIC REPUBLIC", "LA", "LAO", "418", NOW(), "Python"),
        (123, "LATVIA", "LV", "LVA", "428", NOW(), "Python"),
        (124, "LEBANON", "LB", "LBN", "422", NOW(), "Python"),
        (125, "LESOTHO", "LS", "LSO", "426", NOW(), "Python"),
        (126, "LIBERIA", "LR", "LBR", "430", NOW(), "Python"),
        (127, "LIBYA", "LY", "LBY", "434", NOW(), "Python"),
        (128, "LIECHTENSTEIN", "LI", "LIE", "438", NOW(), "Python"),
        (129, "LITHUANIA", "LT", "LTU", "440", NOW(), "Python"),
        (130, "LUXEMBOURG", "LU", "LUX", "442", NOW(), "Python"),
        (131, "MACAO", "MO", "MAC", "446", NOW(), "Python"),
        (132, "MACEDONIA THE FORMER YUGOSLAV REPUBLIC OF", "MK", "MKD", "807", NOW(), "Python"),
        (133, "MADAGASCAR", "MG", "MDG", "450", NOW(), "Python"),
        (134, "MALAWI", "MW", "MWI", "454", NOW(), "Python"),
        (135, "MALAYSIA", "MY", "MYS", "458", NOW(), "Python"),
        (136, "MALDIVES", "MV", "MDV", "462", NOW(), "Python"),
        (137, "MALI", "ML", "MLI", "466", NOW(), "Python"),
        (138, "MALTA", "MT", "MLT", "470", NOW(), "Python"),
        (139, "MARSHALL ISLANDS", "MH", "MHL", "584", NOW(), "Python"),
        (140, "MARTINIQUE", "MQ", "MTQ", "474", NOW(), "Python"),
        (141, "MAURITANIA", "MR", "MRT", "478", NOW(), "Python"),
        (142, "MAURITIUS", "MU", "MUS", "480", NOW(), "Python"),
        (143, "MAYOTTE", "YT", "MYT", "175", NOW(), "Python"),
        (144, "MEXICO", "MX", "MEX", "484", NOW(), "Python"),
        (145, "MICRONESIA FEDERATED STATES OF", "FM", "FSM", "583", NOW(), "Python"),
        (146, "MOLDOVA REPUBLIC OF", "MD", "MDA", "498", NOW(), "Python"),
        (147, "MONACO", "MC", "MCO", "492", NOW(), "Python"),
        (148, "MONGOLIA", "MN", "MNG", "496", NOW(), "Python"),
        (149, "MONTENEGRO", "ME", "MNE", "499", NOW(), "Python"),
        (150, "MONTSERRAT", "MS", "MSR", "500", NOW(), "Python"),
        (151, "MOROCCO", "MA", "MAR", "504", NOW(), "Python"),
        (152, "MOZAMBIQUE", "MZ", "MOZ", "508", NOW(), "Python"),
        (153, "MYANMAR", "MM", "MMR", "104", NOW(), "Python"),
        (154, "NAMIBIA", "NA", "NAM", "516", NOW(), "Python"),
        (155, "NAURU", "NR", "NRU", "520", NOW(), "Python"),
        (156, "NEPAL", "NP", "NPL", "524", NOW(), "Python"),
        (157, "NETHERLANDS", "NL", "NLD", "528", NOW(), "Python"),
        (158, "NEW CALEDONIA", "NC", "NCL", "540", NOW(), "Python"),
        (159, "NEW ZEALAND", "NZ", "NZL", "554", NOW(), "Python"),
        (160, "NICARAGUA", "NI", "NIC", "558", NOW(), "Python"),
        (161, "NIGER", "NE", "NER", "562", NOW(), "Python"),
        (162, "NIGERIA", "NG", "NGA", "566", NOW(), "Python"),
        (163, "NIUE", "NU", "NIU", "570", NOW(), "Python"),
        (164, "NORFOLK ISLAND", "NF", "NFK", "574", NOW(), "Python"),
        (165, "NORTHERN MARIANA ISLANDS", "MP", "MNP", "580", NOW(), "Python"),
        (166, "NORWAY", "NO", "NOR", "578", NOW(), "Python"),
        (167, "OMAN", "OM", "OMN", "512", NOW(), "Python"),
        (168, "PAKISTAN", "PK", "PAK", "586", NOW(), "Python"),
        (169, "PALAU", "PW", "PLW", "585", NOW(), "Python"),
        (170, "PALESTINE, STATE OF", "PS", "PSE", "275", NOW(), "Python"),
        (171, "PANAMA", "PA", "PAN", "591", NOW(), "Python"),
        (172, "PAPUA NEW GUINEA", "PG", "PNG", "598", NOW(), "Python"),
        (173, "PARAGUAY", "PY", "PRY", "600", NOW(), "Python"),
        (174, "PERU", "PE", "PER", "604", NOW(), "Python"),
        (175, "PHILIPPINES", "PH", "PHL", "608", NOW(), "Python"),
        (176, "PITCAIRN", "PN", "PCN", "612", NOW(), "Python"),
        (177, "POLAND", "PL", "POL", "616", NOW(), "Python"),
        (178, "PORTUGAL", "PT", "PRT", "620", NOW(), "Python"),
        (179, "PUERTO RICO", "PR", "PRI", "630", NOW(), "Python"),
        (180, "QATAR", "QA", "QAT", "634", NOW(), "Python"),
        (181, "REUNION", "RE", "REU", "638", NOW(), "Python"),
        (182, "ROMANIA", "RO", "ROU", "642", NOW(), "Python"),
        (183, "RUSSIAN FEDERATION", "RU", "RUS", "643", NOW(), "Python"),
        (184, "RWANDA", "RW", "RWA", "646", NOW(), "Python"),
        (185, "SAINT BARTHELEMY", "BL", "BLM", "652", NOW(), "Python"),
        (186, "SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA", "SH", "SHN", "654", NOW(), "Python"),
        (187, "SAINT KITTS AND NEVIS", "KN", "KNA", "659", NOW(), "Python"),
        (188, "SAINT LUCIA", "LC", "LCA", "662", NOW(), "Python"),
        (189, "SAINT MARTIN FRENCH PART", "MF", "MAF", "663", NOW(), "Python"),
        (190, "SAINT PIERRE AND MIQUELON", "PM", "SPM", "666", NOW(), "Python"),
        (191, "SAINT VINCENT AND THE GRENADINES", "VC", "VCT", "670", NOW(), "Python"),
        (192, "SAMOA", "WS", "WSM", "882", NOW(), "Python"),
        (193, "SAN MARINO", "SM", "SMR", "674", NOW(), "Python"),
        (194, "SAO TOME AND PRINCIPE", "ST", "STP", "678", NOW(), "Python"),
        (195, "SAUDI ARABIA", "SA", "SAU", "682", NOW(), "Python"),
        (196, "SENEGAL", "SN", "SEN", "686", NOW(), "Python"),
        (197, "SERBIA", "RS", "SRB", "688", NOW(), "Python"),
        (198, "SEYCHELLES", "SC", "SYC", "690", NOW(), "Python"),
        (199, "SIERRA LEONE", "SL", "SLE", "694", NOW(), "Python"),
        (200, "SINGAPORE", "SG", "SGP", "702", NOW(), "Python"),
        (201, "SINT MAARTEN DUTCH PART", "SX", "SXM", "534", NOW(), "Python"),
        (202, "SLOVAKIA", "SK", "SVK", "703", NOW(), "Python"),
        (203, "SLOVENIA", "SI", "SVN", "705", NOW(), "Python"),
        (204, "SOLOMON ISLANDS", "SB", "SLB", "90", NOW(), "Python"),
        (205, "SOMALIA", "SO", "SOM", "706", NOW(), "Python"),
        (206, "AFGHANISTAN", "AF", "AFG", "4", NOW(), "Python"),
        (207, "SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS", "GS", "SGS", "239", NOW(), "Python"),
        (208, "SOUTH SUDAN", "SS", "SSD", "728", NOW(), "Python"),
        (209, "SPAIN", "ES", "ESP", "724", NOW(), "Python"),
        (210, "SRI LANKA", "LK", "LKA", "144", NOW(), "Python"),
        (211, "SUDAN", "SD", "SDN", "729", NOW(), "Python"),
        (212, "SURINAME", "SR", "SUR", "740", NOW(), "Python"),
        (213, "SVALBARD AND JAN MAYEN", "SJ", "SJM", "744", NOW(), "Python"),
        (214, "SWAZILAND", "SZ", "SWZ", "748", NOW(), "Python"),
        (215, "SWEDEN", "SE", "SWE", "752", NOW(), "Python"),
        (216, "SWITZERLAND", "CH", "CHE", "756", NOW(), "Python"),
        (217, "SYRIAN ARAB REPUBLIC", "SY", "SYR", "760", NOW(), "Python"),
        (218, "TAIWAN, PROVINCE OF CHINA[A]", "TW", "TWN", "158", NOW(), "Python"),
        (219, "TAJIKISTAN", "TJ", "TJK", "762", NOW(), "Python"),
        (220, "TANZANIA, UNITED REPUBLIC OF", "TZ", "TZA", "834", NOW(), "Python"),
        (221, "THAILAND", "TH", "THA", "764", NOW(), "Python"),
        (222, "TIMOR-LESTE", "TL", "TLS", "626", NOW(), "Python"),
        (223, "TOGO", "TG", "TGO", "768", NOW(), "Python"),
        (224, "TOKELAU", "TK", "TKL", "772", NOW(), "Python"),
        (225, "TONGA", "TO", "TON", "776", NOW(), "Python"),
        (226, "TRINIDAD AND TOBAGO", "TT", "TTO", "780", NOW(), "Python"),
        (227, "TUNISIA", "TN", "TUN", "788", NOW(), "Python"),
        (228, "TURKEY", "TR", "TUR", "792", NOW(), "Python"),
        (229, "TURKMENISTAN", "TM", "TKM", "795", NOW(), "Python"),
        (230, "TURKS AND CAICOS ISLANDS", "TC", "TCA", "796", NOW(), "Python"),
        (231, "TUVALU", "TV", "TUV", "798", NOW(), "Python"),
        (232, "UGANDA", "UG", "UGA", "800", NOW(), "Python"),
        (233, "UKRAINE", "UA", "UKR", "804", NOW(), "Python"),
        (234, "UNITED ARAB EMIRATES", "AE", "ARE", "784", NOW(), "Python"),
        (235, "UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND", "GB", "GBR", "826", NOW(), "Python"),
        (236, "UNITED STATES OF AMERICA", "US", "USA", "840", NOW(), "Python"),
        (237, "UNITED STATES MINOR OUTLYING ISLANDS", "UM", "UMI", "581", NOW(), "Python"),
        (238, "URUGUAY", "UY", "URY", "858", NOW(), "Python"),
        (239, "UZBEKISTAN", "UZ", "UZB", "860", NOW(), "Python"),
        (240, "VANUATU", "VU", "VUT", "548", NOW(), "Python"),
        (241, "VENEZUELA BOLIVARIAN REPUBLIC OF", "VE", "VEN", "862", NOW(), "Python"),
        (242, "VIET NAM", "VN", "VNM", "704", NOW(), "Python"),
        (243, "VIRGIN ISLANDS BRITISH", "VG", "VGB", "92", NOW(), "Python"),
        (244, "VIRGIN ISLANDS U.S.", "VI", "VIR", "850", NOW(), "Python"),
        (245, "WALLIS AND FUTUNA", "WF", "WLF", "876", NOW(), "Python"),
        (246, "WESTERN SAHARA", "EH", "ESH", "732", NOW(), "Python"),
        (247, "YEMEN", "YE", "YEM", "887", NOW(), "Python"),
        (248, "ZAMBIA", "ZM", "ZMB", "894", NOW(), "Python"),
        (249, "ZIMBABWE", "ZW", "ZWE", "716", NOW(), "Python")
        """ + ";"
        s_sql = s_sql.replace("%TABLE%", s_table)
        curs.execute(s_sql)
        cnxn.commit()
        funcfile.writelog("%t INSERTED DATA: SYS_COUNTRIES(" + s_table + ")")

    # ******************************************************************************

    # Script log file
    funcfile.writelog("-------------------------------")
    funcfile.writelog("COMPLETED: WEB_SYSTEM_COUNTRIES")

    return


if __name__ == '__main__':
    try:
        sys_countries()
        # Test automated function - delete and create new table with data
        # sys_users("Web_tax_admin", "y", "y")
    finally:
        print("")
