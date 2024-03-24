Select
    Case
        When usr.block = 0
        Then Concat(cus.name, ' (Active)')
        Else Concat(cus.name, ' (Inactive)')
    End As customer,
    usr.id As user_id,
    con.id As contact_id,
    usr.name As user,
    usr.username As username,
    con.telephone As telephone,
    concat('<a href = "mailto: ', lower(usr.email), '">', lower(usr.email), '</a>') As email,
    usr.registerDate As register_date,
    usr.lastvisitDate As visit_date,
    Case
        When usr.block = 0
        Then ''
        Else adu.active_to
    End As inactive_date,
    usg.title As user_group,
    Concat('<a href = "index.php?option=com_rsform&formId=', adu.form_edit_id, '&id=', usr.id, '&action=edit">Edit</a>') As actions    
From
    tax_users usr Inner Join
    sys_user_map map On map.system_id = usr.id Inner Join
    tax_contact_details con On con.id = map.contact_id Left Join
    tax_contact_details cus On cus.id = map.customer_id Left Join
    sys_user adu On adu.system_id = usr.id Inner Join
    tax_user_usergroup_map usm On usm.user_id = usr.id Inner Join
    tax_usergroups usg On usg.id = usm.group_id
Group By
    cus.name,
    usr.block,
    usr.username,
    usg.title
