Select
    db.customer_id,
    db.name,
    db.description,
    db.active_from,
    db.active_to
From
    sys_client_type db
Where
    -- db.client_type_id  = '". $id."'
    db.client_type_id = 1