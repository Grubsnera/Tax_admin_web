Select
    c.country_name,
    t.town_name,
    t.town_suburb,
    t.town_dialcode,
    t.town_postcode,
    t.town_coordinates,
    Concat('<a href = "index.php?option=com_rsform&formId=', t.form_edit_id, '&id=0', '&action=add">Add</a>', ' | ',
    '<a href = "index.php?option=com_rsform&formId=', t.form_edit_id, '&id=', t.town_id, '&action=edit">Edit</a>',
    ' | ', '<a href = "index.php?option=com_rsform&formId=', t.form_edit_id, '&id=', t.town_id,
    '&action=copy">Copy</a>') As actions
From
    sys_town t Inner Join
    sys_country c On c.country_iso2 = t.country_iso2
Where
    -- t.town_name like ('%{user_param_1:cmd}%')  
    t.town_name like ('%potch%')
Group By
    c.country_name,
    t.town_name,
    t.town_suburb