Select
    coun.country_name,
    coun.country_iso2,
    coun.country_iso3,
    coun.country_ison,
    coun.country_dialcode,
    coun.country_timezone,
    Concat('<a href = "index.php?option=com_rsform&formId=', coun.form_edit_id, '&id=0', '&action=add">Add</a>', ' | ',
    '<a href = "index.php?option=com_rsform&formId=', coun.form_edit_id, '&id=', coun.country_id,
    '&action=edit">Edit</a>', ' | ', '<a href = "index.php?option=com_rsform&formId=', coun.form_edit_id, '&id=',
    coun.country_id, '&action=copy">Copy</a>', ' | ', '<a href = "index.php?option=com_rsform&formId=',
    coun.form_edit_id, '&id=', coun.country_id, '&action=delete">Delete</a>') As actions
From
    sys_country coun
Group By
    coun.country_name