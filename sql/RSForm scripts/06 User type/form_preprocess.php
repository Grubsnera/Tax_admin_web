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

// Populate the form fields with data from the parameters
$val['id'] = $id;
$val['action'] = $action;

// Fill the form if record number is given
// Edit, copy and delete, except add
if ($id > 0) {

	// Build the query
	$query = "
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

	// Populate the form fields with data read from the table
	if ($action == 'copy') {
		$val['name'] = $result->name.' - COPY';
	} else {
		$val['name'] = $result->name;
	}
	
	$val['customer'] = $result->customer_id;
	$val['description'] = $result->description;
	$val['from'] = date('Y-m-d', strtotime($result->active_from));
	$val['to'] = date('Y-m-d', strtotime($result->active_to));

};

?>