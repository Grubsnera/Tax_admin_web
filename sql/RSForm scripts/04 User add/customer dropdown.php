<?php
//<code>

// Get the user object
$user = JFactory::getUser();

// Exit if the user is not logged in
if ($user->guest) {
return '|Error (login first)[c]';
}

// Get the user id
$user_id = $user->get('id');
// echo 'User ID: '.$user_id.'<br>';

// Check if the user belongs to the "Super Users" group
$superUserGroup = 8; // ID of the "Super Users" group
$isSuperUser = $user->groups && in_array($superUserGroup, $user->groups) ? true : false;
// echo 'Super user: '.$isSuperUser.'<br>';

// Obtain the session client id
$customer_id = 0;
if (isset($_SESSION['customer_id'])) {
	$customer_id = $_SESSION['customer_id'];
}
// echo 'Client ID: '.$customer_id.'<br>';

// Test for a valid customer_id
if ($isSuperUser) {
} elseif ($customer_id > 0) {
} else {
    return '|Error (login first)[c]';
};

// Prepare dropdown data
// Build the query

if ($isSuperUser) {

	// Display all customers to the super user
	$query = "
	Select
		cont.id As value,
		cont.name As label
	From
		tax_contact_details cont Inner Join
		tax_categories cate On cate.id = cont.catid
	Where
		cate.extension = 'com_contact' And
		cate.title = 'Customer'
	";

	// Add a please select
	$items[] = "|Please Select[c]";

} else {

	// Display only the customer to which the user belongs
	$query = "
	Select
		cont.id As value,
		cont.name As label
	From
		tax_contact_details cont Inner Join
		tax_categories cate On cate.id = cont.catid
	Where
		cate.extension = 'com_contact' And
		cate.title = 'Customer' And
		cont.id = ".$customer_id."
	";
}

// Query the database
// echo 'SQL Query: '.$query.'<br>';
$db = JFactory::getDbo();
$db->setQuery($query);
$results = $db->loadObjectList();

// Format for RSForm! Pro dropdown format.
foreach ($results as $result) {
	$items[] = $result->value.'|'.$result->label;
}

// Now we need to return the value to the field
return $items;

//</code>
?>