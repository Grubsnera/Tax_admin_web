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
    `coun_id` int(11) NOT NULL AUTO_INCREMENT,
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
        `coun_name`,
        `coun_iso2`,
        `coun_iso3`,
        `coun_ison`,
        `created`,
        `created_by_alias`
        )
        VALUES
        ("SOUTH AFRICA", "ZA", "ZAF", "710", NOW(), "Python"),
        ("AFGHANISTAN", "AF", "AFG", "4", NOW(), "Python"),
        ("ALAND ISLANDS", "AX", "ALA", "248", NOW(), "Python"),
        ("ALBANIA", "AL", "ALB", "8", NOW(), "Python"),
        ("ALGERIA", "DZ", "DZA", "12", NOW(), "Python"),
        ("AMERICAN SAMOA", "AS", "ASM", "16", NOW(), "Python"),
        ("ANDORRA", "AD", "AND", "20", NOW(), "Python"),
        ("ANGOLA", "AO", "AGO", "24", NOW(), "Python"),
        ("ANGUILLA", "AI", "AIA", "660", NOW(), "Python"),
        ("ANTARCTICA", "AQ", "ATA", "10", NOW(), "Python"),
        ("ANTIGUA AND BARBUDA", "AG", "ATG", "28", NOW(), "Python"),
        ("ARGENTINA", "AR", "ARG", "32", NOW(), "Python"),
        ("ARMENIA", "AM", "ARM", "51", NOW(), "Python"),
        ("ARUBA", "AW", "ABW", "533", NOW(), "Python"),
        ("AUSTRALIA", "AU", "AUS", "36", NOW(), "Python"),
        ("AUSTRIA", "AT", "AUT", "40", NOW(), "Python"),
        ("AZERBAIJAN", "AZ", "AZE", "31", NOW(), "Python"),
        ("BAHAMAS", "BS", "BHS", "44", NOW(), "Python"),
        ("BAHRAIN", "BH", "BHR", "48", NOW(), "Python"),
        ("BANGLADESH", "BD", "BGD", "50", NOW(), "Python"),
        ("BARBADOS", "BB", "BRB", "52", NOW(), "Python"),
        ("BELARUS", "BY", "BLR", "112", NOW(), "Python"),
        ("BELGIUM", "BE", "BEL", "56", NOW(), "Python"),
        ("BELIZE", "BZ", "BLZ", "84", NOW(), "Python"),
        ("BENIN", "BJ", "BEN", "204", NOW(), "Python"),
        ("BERMUDA", "BM", "BMU", "60", NOW(), "Python"),
        ("BHUTAN", "BT", "BTN", "64", NOW(), "Python"),
        ("BOLIVIA PLURINATIONAL STATE OF", "BO", "BOL", "68", NOW(), "Python"),
        ("BONAIRE, SINT EUSTATIUS AND SABA", "BQ", "BES", "535", NOW(), "Python"),
        ("BOSNIA AND HERZEGOVINA", "BA", "BIH", "70", NOW(), "Python"),
        ("BOTSWANA", "BW", "BWA", "72", NOW(), "Python"),
        ("BOUVET ISLAND", "BV", "BVT", "74", NOW(), "Python"),
        ("BRAZIL", "BR", "BRA", "76", NOW(), "Python"),
        ("BRITISH INDIAN OCEAN TERRITORY", "IO", "IOT", "86", NOW(), "Python"),
        ("BRUNEI DARUSSALAM", "BN", "BRN", "96", NOW(), "Python"),
        ("BULGARIA", "BG", "BGR", "100", NOW(), "Python"),
        ("BURKINA FASO", "BF", "BFA", "854", NOW(), "Python"),
        ("BURUNDI", "BI", "BDI", "108", NOW(), "Python"),
        ("CABO VERDE", "CV", "CPV", "132", NOW(), "Python"),
        ("CAMBODIA", "KH", "KHM", "116", NOW(), "Python"),
        ("CAMEROON", "CM", "CMR", "120", NOW(), "Python"),
        ("CANADA", "CA", "CAN", "124", NOW(), "Python"),
        ("CAYMAN ISLANDS", "KY", "CYM", "136", NOW(), "Python"),
        ("CENTRAL AFRICAN REPUBLIC", "CF", "CAF", "140", NOW(), "Python"),
        ("CHAD", "TD", "TCD", "148", NOW(), "Python"),
        ("CHILE", "CL", "CHL", "152", NOW(), "Python"),
        ("CHINA", "CN", "CHN", "156", NOW(), "Python"),
        ("CHRISTMAS ISLAND", "CX", "CXR", "162", NOW(), "Python"),
        ("COCOS KEELING ISLANDS", "CC", "CCK", "166", NOW(), "Python"),
        ("COLOMBIA", "CO", "COL", "170", NOW(), "Python"),
        ("COMOROS", "KM", "COM", "174", NOW(), "Python"),
        ("CONGO", "CG", "COG", "178", NOW(), "Python"),
        ("CONGO DEMOCRATIC REPUBLIC OF THE", "CD", "COD", "180", NOW(), "Python"),
        ("COOK ISLANDS", "CK", "COK", "184", NOW(), "Python"),
        ("COSTA RICA", "CR", "CRI", "188", NOW(), "Python"),
        ("COTE DIVOIRE", "CI", "CIV", "384", NOW(), "Python"),
        ("CROATIA", "HR", "HRV", "191", NOW(), "Python"),
        ("CUBA", "CU", "CUB", "192", NOW(), "Python"),
        ("CURACAO", "CW", "CUW", "531", NOW(), "Python"),
        ("CYPRUS", "CY", "CYP", "196", NOW(), "Python"),
        ("CZECH REPUBLIC", "CZ", "CZE", "203", NOW(), "Python"),
        ("DENMARK", "DK", "DNK", "208", NOW(), "Python"),
        ("DJIBOUTI", "DJ", "DJI", "262", NOW(), "Python"),
        ("DOMINICA", "DM", "DMA", "212", NOW(), "Python"),
        ("DOMINICAN REPUBLIC", "DO", "DOM", "214", NOW(), "Python"),
        ("ECUADOR", "EC", "ECU", "218", NOW(), "Python"),
        ("EGYPT", "EG", "EGY", "818", NOW(), "Python"),
        ("EL SALVADOR", "SV", "SLV", "222", NOW(), "Python"),
        ("EQUATORIAL GUINEA", "GQ", "GNQ", "226", NOW(), "Python"),
        ("ERITREA", "ER", "ERI", "232", NOW(), "Python"),
        ("ESTONIA", "EE", "EST", "233", NOW(), "Python"),
        ("ETHIOPIA", "ET", "ETH", "231", NOW(), "Python"),
        ("FALKLAND ISLANDS MALVINAS", "FK", "FLK", "238", NOW(), "Python"),
        ("FAROE ISLANDS", "FO", "FRO", "234", NOW(), "Python"),
        ("FIJI", "FJ", "FJI", "242", NOW(), "Python"),
        ("FINLAND", "FI", "FIN", "246", NOW(), "Python"),
        ("FRANCE", "FR", "FRA", "250", NOW(), "Python"),
        ("FRENCH GUIANA", "GF", "GUF", "254", NOW(), "Python"),
        ("FRENCH POLYNESIA", "PF", "PYF", "258", NOW(), "Python"),
        ("FRENCH SOUTHERN TERRITORIES", "TF", "ATF", "260", NOW(), "Python"),
        ("GABON", "GA", "GAB", "266", NOW(), "Python"),
        ("GAMBIA", "GM", "GMB", "270", NOW(), "Python"),
        ("GEORGIA", "GE", "GEO", "268", NOW(), "Python"),
        ("GERMANY", "DE", "DEU", "276", NOW(), "Python"),
        ("GHANA", "GH", "GHA", "288", NOW(), "Python"),
        ("GIBRALTAR", "GI", "GIB", "292", NOW(), "Python"),
        ("GREECE", "GR", "GRC", "300", NOW(), "Python"),
        ("GREENLAND", "GL", "GRL", "304", NOW(), "Python"),
        ("GRENADA", "GD", "GRD", "308", NOW(), "Python"),
        ("GUADELOUPE", "GP", "GLP", "312", NOW(), "Python"),
        ("GUAM", "GU", "GUM", "316", NOW(), "Python"),
        ("GUATEMALA", "GT", "GTM", "320", NOW(), "Python"),
        ("GUERNSEY", "GG", "GGY", "831", NOW(), "Python"),
        ("GUINEA", "GN", "GIN", "324", NOW(), "Python"),
        ("GUINEA-BISSAU", "GW", "GNB", "624", NOW(), "Python"),
        ("GUYANA", "GY", "GUY", "328", NOW(), "Python"),
        ("HAITI", "HT", "HTI", "332", NOW(), "Python"),
        ("HEARD ISLAND AND MCDONALD ISLANDS", "HM", "HMD", "334", NOW(), "Python"),
        ("HOLY SEE", "VA", "VAT", "336", NOW(), "Python"),
        ("HONDURAS", "HN", "HND", "340", NOW(), "Python"),
        ("HONG KONG", "HK", "HKG", "344", NOW(), "Python"),
        ("HUNGARY", "HU", "HUN", "348", NOW(), "Python"),
        ("ICELAND", "IS", "ISL", "352", NOW(), "Python"),
        ("INDIA", "IN", "IND", "356", NOW(), "Python"),
        ("INDONESIA", "ID", "IDN", "360", NOW(), "Python"),
        ("IRAN ISLAMIC REPUBLIC OF", "IR", "IRN", "364", NOW(), "Python"),
        ("IRAQ", "IQ", "IRQ", "368", NOW(), "Python"),
        ("IRELAND", "IE", "IRL", "372", NOW(), "Python"),
        ("ISLE OF MAN", "IM", "IMN", "833", NOW(), "Python"),
        ("ISRAEL", "IL", "ISR", "376", NOW(), "Python"),
        ("ITALY", "IT", "ITA", "380", NOW(), "Python"),
        ("JAMAICA", "JM", "JAM", "388", NOW(), "Python"),
        ("JAPAN", "JP", "JPN", "392", NOW(), "Python"),
        ("JERSEY", "JE", "JEY", "832", NOW(), "Python"),
        ("JORDAN", "JO", "JOR", "400", NOW(), "Python"),
        ("KAZAKHSTAN", "KZ", "KAZ", "398", NOW(), "Python"),
        ("KENYA", "KE", "KEN", "404", NOW(), "Python"),
        ("KIRIBATI", "KI", "KIR", "296", NOW(), "Python"),
        ("KOREA DEMOCRATIC PEOPLES REPUBLIC OF", "KP", "PRK", "408", NOW(), "Python"),
        ("KOREA REPUBLIC OF", "KR", "KOR", "410", NOW(), "Python"),
        ("KUWAIT", "KW", "KWT", "414", NOW(), "Python"),
        ("KYRGYZSTAN", "KG", "KGZ", "417", NOW(), "Python"),
        ("LAO PEOPLES DEMOCRATIC REPUBLIC", "LA", "LAO", "418", NOW(), "Python"),
        ("LATVIA", "LV", "LVA", "428", NOW(), "Python"),
        ("LEBANON", "LB", "LBN", "422", NOW(), "Python"),
        ("LESOTHO", "LS", "LSO", "426", NOW(), "Python"),
        ("LIBERIA", "LR", "LBR", "430", NOW(), "Python"),
        ("LIBYA", "LY", "LBY", "434", NOW(), "Python"),
        ("LIECHTENSTEIN", "LI", "LIE", "438", NOW(), "Python"),
        ("LITHUANIA", "LT", "LTU", "440", NOW(), "Python"),
        ("LUXEMBOURG", "LU", "LUX", "442", NOW(), "Python"),
        ("MACAO", "MO", "MAC", "446", NOW(), "Python"),
        ("MACEDONIA THE FORMER YUGOSLAV REPUBLIC OF", "MK", "MKD", "807", NOW(), "Python"),
        ("MADAGASCAR", "MG", "MDG", "450", NOW(), "Python"),
        ("MALAWI", "MW", "MWI", "454", NOW(), "Python"),
        ("MALAYSIA", "MY", "MYS", "458", NOW(), "Python"),
        ("MALDIVES", "MV", "MDV", "462", NOW(), "Python"),
        ("MALI", "ML", "MLI", "466", NOW(), "Python"),
        ("MALTA", "MT", "MLT", "470", NOW(), "Python"),
        ("MARSHALL ISLANDS", "MH", "MHL", "584", NOW(), "Python"),
        ("MARTINIQUE", "MQ", "MTQ", "474", NOW(), "Python"),
        ("MAURITANIA", "MR", "MRT", "478", NOW(), "Python"),
        ("MAURITIUS", "MU", "MUS", "480", NOW(), "Python"),
        ("MAYOTTE", "YT", "MYT", "175", NOW(), "Python"),
        ("MEXICO", "MX", "MEX", "484", NOW(), "Python"),
        ("MICRONESIA FEDERATED STATES OF", "FM", "FSM", "583", NOW(), "Python"),
        ("MOLDOVA REPUBLIC OF", "MD", "MDA", "498", NOW(), "Python"),
        ("MONACO", "MC", "MCO", "492", NOW(), "Python"),
        ("MONGOLIA", "MN", "MNG", "496", NOW(), "Python"),
        ("MONTENEGRO", "ME", "MNE", "499", NOW(), "Python"),
        ("MONTSERRAT", "MS", "MSR", "500", NOW(), "Python"),
        ("MOROCCO", "MA", "MAR", "504", NOW(), "Python"),
        ("MOZAMBIQUE", "MZ", "MOZ", "508", NOW(), "Python"),
        ("MYANMAR", "MM", "MMR", "104", NOW(), "Python"),
        ("NAMIBIA", "NA", "NAM", "516", NOW(), "Python"),
        ("NAURU", "NR", "NRU", "520", NOW(), "Python"),
        ("NEPAL", "NP", "NPL", "524", NOW(), "Python"),
        ("NETHERLANDS", "NL", "NLD", "528", NOW(), "Python"),
        ("NEW CALEDONIA", "NC", "NCL", "540", NOW(), "Python"),
        ("NEW ZEALAND", "NZ", "NZL", "554", NOW(), "Python"),
        ("NICARAGUA", "NI", "NIC", "558", NOW(), "Python"),
        ("NIGER", "NE", "NER", "562", NOW(), "Python"),
        ("NIGERIA", "NG", "NGA", "566", NOW(), "Python"),
        ("NIUE", "NU", "NIU", "570", NOW(), "Python"),
        ("NORFOLK ISLAND", "NF", "NFK", "574", NOW(), "Python"),
        ("NORTHERN MARIANA ISLANDS", "MP", "MNP", "580", NOW(), "Python"),
        ("NORWAY", "NO", "NOR", "578", NOW(), "Python"),
        ("OMAN", "OM", "OMN", "512", NOW(), "Python"),
        ("PAKISTAN", "PK", "PAK", "586", NOW(), "Python"),
        ("PALAU", "PW", "PLW", "585", NOW(), "Python"),
        ("PALESTINE, STATE OF", "PS", "PSE", "275", NOW(), "Python"),
        ("PANAMA", "PA", "PAN", "591", NOW(), "Python"),
        ("PAPUA NEW GUINEA", "PG", "PNG", "598", NOW(), "Python"),
        ("PARAGUAY", "PY", "PRY", "600", NOW(), "Python"),
        ("PERU", "PE", "PER", "604", NOW(), "Python"),
        ("PHILIPPINES", "PH", "PHL", "608", NOW(), "Python"),
        ("PITCAIRN", "PN", "PCN", "612", NOW(), "Python"),
        ("POLAND", "PL", "POL", "616", NOW(), "Python"),
        ("PORTUGAL", "PT", "PRT", "620", NOW(), "Python"),
        ("PUERTO RICO", "PR", "PRI", "630", NOW(), "Python"),
        ("QATAR", "QA", "QAT", "634", NOW(), "Python"),
        ("REUNION", "RE", "REU", "638", NOW(), "Python"),
        ("ROMANIA", "RO", "ROU", "642", NOW(), "Python"),
        ("RUSSIAN FEDERATION", "RU", "RUS", "643", NOW(), "Python"),
        ("RWANDA", "RW", "RWA", "646", NOW(), "Python"),
        ("SAINT BARTHELEMY", "BL", "BLM", "652", NOW(), "Python"),
        ("SAINT HELENA, ASCENSION AND TRISTAN DA CUNHA", "SH", "SHN", "654", NOW(), "Python"),
        ("SAINT KITTS AND NEVIS", "KN", "KNA", "659", NOW(), "Python"),
        ("SAINT LUCIA", "LC", "LCA", "662", NOW(), "Python"),
        ("SAINT MARTIN FRENCH PART", "MF", "MAF", "663", NOW(), "Python"),
        ("SAINT PIERRE AND MIQUELON", "PM", "SPM", "666", NOW(), "Python"),
        ("SAINT VINCENT AND THE GRENADINES", "VC", "VCT", "670", NOW(), "Python"),
        ("SAMOA", "WS", "WSM", "882", NOW(), "Python"),
        ("SAN MARINO", "SM", "SMR", "674", NOW(), "Python"),
        ("SAO TOME AND PRINCIPE", "ST", "STP", "678", NOW(), "Python"),
        ("SAUDI ARABIA", "SA", "SAU", "682", NOW(), "Python"),
        ("SENEGAL", "SN", "SEN", "686", NOW(), "Python"),
        ("SERBIA", "RS", "SRB", "688", NOW(), "Python"),
        ("SEYCHELLES", "SC", "SYC", "690", NOW(), "Python"),
        ("SIERRA LEONE", "SL", "SLE", "694", NOW(), "Python"),
        ("SINGAPORE", "SG", "SGP", "702", NOW(), "Python"),
        ("SINT MAARTEN DUTCH PART", "SX", "SXM", "534", NOW(), "Python"),
        ("SLOVAKIA", "SK", "SVK", "703", NOW(), "Python"),
        ("SLOVENIA", "SI", "SVN", "705", NOW(), "Python"),
        ("SOLOMON ISLANDS", "SB", "SLB", "90", NOW(), "Python"),
        ("SOMALIA", "SO", "SOM", "706", NOW(), "Python"),
        ("SOUTH GEORGIA AND THE SOUTH SANDWICH ISLANDS", "GS", "SGS", "239", NOW(), "Python"),
        ("SOUTH SUDAN", "SS", "SSD", "728", NOW(), "Python"),
        ("SPAIN", "ES", "ESP", "724", NOW(), "Python"),
        ("SRI LANKA", "LK", "LKA", "144", NOW(), "Python"),
        ("SUDAN", "SD", "SDN", "729", NOW(), "Python"),
        ("SURINAME", "SR", "SUR", "740", NOW(), "Python"),
        ("SVALBARD AND JAN MAYEN", "SJ", "SJM", "744", NOW(), "Python"),
        ("SWAZILAND", "SZ", "SWZ", "748", NOW(), "Python"),
        ("SWEDEN", "SE", "SWE", "752", NOW(), "Python"),
        ("SWITZERLAND", "CH", "CHE", "756", NOW(), "Python"),
        ("SYRIAN ARAB REPUBLIC", "SY", "SYR", "760", NOW(), "Python"),
        ("TAIWAN, PROVINCE OF CHINA[A]", "TW", "TWN", "158", NOW(), "Python"),
        ("TAJIKISTAN", "TJ", "TJK", "762", NOW(), "Python"),
        ("TANZANIA, UNITED REPUBLIC OF", "TZ", "TZA", "834", NOW(), "Python"),
        ("THAILAND", "TH", "THA", "764", NOW(), "Python"),
        ("TIMOR-LESTE", "TL", "TLS", "626", NOW(), "Python"),
        ("TOGO", "TG", "TGO", "768", NOW(), "Python"),
        ("TOKELAU", "TK", "TKL", "772", NOW(), "Python"),
        ("TONGA", "TO", "TON", "776", NOW(), "Python"),
        ("TRINIDAD AND TOBAGO", "TT", "TTO", "780", NOW(), "Python"),
        ("TUNISIA", "TN", "TUN", "788", NOW(), "Python"),
        ("TURKEY", "TR", "TUR", "792", NOW(), "Python"),
        ("TURKMENISTAN", "TM", "TKM", "795", NOW(), "Python"),
        ("TURKS AND CAICOS ISLANDS", "TC", "TCA", "796", NOW(), "Python"),
        ("TUVALU", "TV", "TUV", "798", NOW(), "Python"),
        ("UGANDA", "UG", "UGA", "800", NOW(), "Python"),
        ("UKRAINE", "UA", "UKR", "804", NOW(), "Python"),
        ("UNITED ARAB EMIRATES", "AE", "ARE", "784", NOW(), "Python"),
        ("UNITED KINGDOM OF GREAT BRITAIN AND NORTHERN IRELAND", "GB", "GBR", "826", NOW(), "Python"),
        ("UNITED STATES OF AMERICA", "US", "USA", "840", NOW(), "Python"),
        ("UNITED STATES MINOR OUTLYING ISLANDS", "UM", "UMI", "581", NOW(), "Python"),
        ("URUGUAY", "UY", "URY", "858", NOW(), "Python"),
        ("UZBEKISTAN", "UZ", "UZB", "860", NOW(), "Python"),
        ("VANUATU", "VU", "VUT", "548", NOW(), "Python"),
        ("VENEZUELA BOLIVARIAN REPUBLIC OF", "VE", "VEN", "862", NOW(), "Python"),
        ("VIET NAM", "VN", "VNM", "704", NOW(), "Python"),
        ("VIRGIN ISLANDS BRITISH", "VG", "VGB", "92", NOW(), "Python"),
        ("VIRGIN ISLANDS U.S.", "VI", "VIR", "850", NOW(), "Python"),
        ("WALLIS AND FUTUNA", "WF", "WLF", "876", NOW(), "Python"),
        ("WESTERN SAHARA", "EH", "ESH", "732", NOW(), "Python"),
        ("YEMEN", "YE", "YEM", "887", NOW(), "Python"),
        ("ZAMBIA", "ZM", "ZMB", "894", NOW(), "Python"),
        ("ZIMBABWE", "ZW", "ZWE", "716", NOW(), "Python")
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
