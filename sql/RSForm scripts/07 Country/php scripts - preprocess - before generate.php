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
        c.country_id,
        c.country_name,
        c.country_iso2,
        c.country_iso3,
        c.country_ison,
        c.country_dialcode,
        c.country_timezone
    From
        sys_country c
    Where
        -- c.country_id = ".$id."
        c.country_id = 1
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
        $val['name'] = $result->country_name.' - COPY';
    } else {
        $val['name'] = $result->country_name;
    }
    $val['iso2'] = $result->country_iso2;
    $val['iso3'] = $result->country_iso3;
    $val['ison'] = $result->country_ison;
    $val['dial'] = $result->country_dialcode;
    $val['zone'] = $result->country_timezone;
    //$val[''] = $result->;
    //$val[''] = date('Y-m-d', strtotime($result->));

};

?>