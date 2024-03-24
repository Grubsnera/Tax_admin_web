Select
    Case
        When Now() Between type.active_from And type.active_to
        Then Concat(cont.name, ' (Active)')
        Else Concat(cont.name, ' (Inactive)')
    End As customer,
    type.name As name,
    type.description,
    type.active_from,
    type.active_to,
    Concat('<a href = "index.php?option=com_rsform&formId=', type.form_edit_id, '&id=0', '&action=add">Add</a>', ' | ',
    '<a href = "index.php?option=com_rsform&formId=', type.form_edit_id, '&id=', type.client_type_id,
    '&action=edit">Edit</a>', ' | ', '<a href = "index.php?option=com_rsform&formId=', type.form_edit_id, '&id=',
    type.client_type_id, '&action=copy">Copy</a>', ' | ', '<a href = "index.php?option=com_rsform&formId=',
    type.form_edit_id, '&id=', type.client_type_id, '&action=delete">Delete</a>') As actions
From
    sys_client_type type Inner Join
    tax_contact_details cont On cont.id = type.customer_id
Group By
    Case
        When Now() Between type.active_from And type.active_to
        Then Concat(cont.name, ' (Active)')
        Else Concat(cont.name, ' (Inactive)')
    End,
    type.name