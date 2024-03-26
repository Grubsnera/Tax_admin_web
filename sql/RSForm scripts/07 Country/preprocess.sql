Select
    c.country_id,
    c.country_name,
    c.country_iso2,
    c.country_iso3,
    c.country_ison,
    c.country_dialcode,
    c.country_timezone
From
    sys_country c
Where
    -- c.country_id = ".$id."
    c.country_id = 1