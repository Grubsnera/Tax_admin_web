Select
    t.town_id,
    t.town_name,
    t.town_suburb,
    t.town_dialcode,
    t.town_postcode,
    t.town_coordinates,
    t.country_iso2
From
    sys_town t
Where
    -- t.town_id = ".$id."
    t.town_id = 1