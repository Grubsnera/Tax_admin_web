	Select
		cont.id As value,
		cont.name As label
	From
		tax_contact_details cont Inner Join
		tax_categories cate On cate.id = cont.catid
	Where
		cate.extension = 'com_contact' And
		cate.title = 'Customer'