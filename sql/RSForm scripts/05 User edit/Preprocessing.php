<?php

// Get the form parameters
$id = JFactory::getApplication()->input->getString('id');
$action = JFactory::getApplication()->input->getString('action');

// Exit page if no id was supplied
$id_test = "-".$id."-";
if ($id_test == '--') {
	$mess = 'You are not authorised to view this page!';
	$mess .= "Web Administrator";
die($mess);
}

// Populate the form fields with data read from the table
$val['user_id'] = $id;
$val['action'] = $action;

// Fill the form when edit or copy
if ($id > 0) {

	// Build the query
	$query = "
    Select
        umap.customer_id,
        user.name,
        user.username,
        cont.con_position,
        user.email,
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
	";

	// Open a local database
	$db = JFactory::getDbo();
	$db->setQuery($query);
	$results = $db->loadObjectList();

	// Do a test to see if form is still valid
	if (empty($results)) {
		$mess = "The database record no longer exist!\n";
		$mess .= "Web Administrator";
	die($mess);
	}

	// Get the result
	$result = $results[0];

	// Populate the form fields with data read from the table\
	$val['customer'] = $result->customer_id;
	$val['name'] = $result->name;
	$val['username'] = $result->username;
	$val['position'] = $result->con_position;
	$val['email'] = $result->email;
	$val['telephone'] = $result->telephone;
	$val['mobile'] = $result->mobile;
	$val['group'] = $result->group_id;
	$val['reset'] = $result->requireReset;
	$val['block'] = $result->block;
	$val['active'] = $result->active_to;
	$val['misc'] = $result->misc;

};

//$val[''] = $result->;
//$val[''] = date('Y-m-d', strtotime($result->));


?>