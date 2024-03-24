<?php

// Script to obtain the logged in user id and name
// Based on this data, the ia_user_map and jm4_contact_details table
// are used to identify the web customer (company) id and name.
// The customer variables are then store in the session to use everywhere while the session is going.

// Obtain the current user
$user = JFactory::getUser();
$user_id = $user->get('id');
$user_name = $user->get('name');
$db = JFactory::getDbo();

// Obtain the client id
$sql = "
Select
	umap.customer_id,
	cont.name
From
	sys_user_map umap Inner Join
	tax_contact_details cont On cont.id = umap.customer_id
Where
	umap.system_id = '".$user_id."' limit 1
";
$db->setQuery($sql);
$results = $db->loadObjectList();

// Store the contact to a varialbe in the current session
foreach ($results as $result) {
	$customer_id = $result->customer_id;
	$customer_name = $result->name;
	$_SESSION['customer_id'] = $customer_id;
	$_SESSION['customer_name'] = $customer_name;
}

// Display customer and user details
if ($user_name <> "") {
	echo "<h2>".$customer_name."</h2>";
	echo "Wecome <strong>".$user_name."!</strong> Hope you enjoy your time here.<br/>";
} else {
	echo "Welcome! You will need to sign in to your account to continue.";
}

?>