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
        t.town_id,
        t.town_name,
        t.town_suburb,
        t.town_dialcode,
        t.town_postcode,
        t.town_coordinates,
        t.country_iso2
    From
        sys_town t
    Where
        t.town_id = ".$id."
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
        $val['name'] = $result->town_name.' - COPY';
    } else {
        $val['name'] = $result->town_name;
    }
    $val['country'] = $result->country_iso2;
    $val['suburb'] = $result->town_suburb;
    $val['dial'] = $result->town_dialcode;
    $val['post'] = $result->town_postcode;
    $val['coordinate'] = $result->town_coordinates;
    //$val[''] = $result->;
    //$val[''] = date('Y-m-d', strtotime($result->));

};

?>