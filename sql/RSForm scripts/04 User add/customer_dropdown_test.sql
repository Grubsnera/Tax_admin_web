Select
    cont.id,
    cont.name,
    cate.extension,
    cate.title
From
    tax_contact_details cont Inner Join
    tax_categories cate On cate.id = cont.catid