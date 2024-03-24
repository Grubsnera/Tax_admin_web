Select
    umap.customer_id,
    user.name,
    user.username,
    user.email,
    cont.con_position,
    cont.telephone,
    cont.mobile,
    gmap.group_id,
    user.requireReset,
    user.block,
    sys_user.active_to,
    cont.misc
From
    tax_users user Inner Join
    tax_user_usergroup_map gmap On gmap.user_id = user.id Inner Join
    tax_contact_details cont On cont.user_id = user.id Inner Join
    sys_user_map umap On umap.system_id = user.id Inner Join
    sys_user On sys_user.system_id = user.id
Where
	-- user.id = '". $id."'
    user.id = 486