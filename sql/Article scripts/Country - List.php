<?php

// Script to display a list of countries

// Get the current user
$user = JFactory::getUser();

// Check if the user belongs to the "Super Users" group
$superUserGroup = 8; // ID of the "Super Users" group
$isSuperUser = $user->groups && in_array($superUserGroup, $user->groups) ? true : false;

// Get the customer id
$customer_id = $_SESSION['customer_id'];

// Use the $isSuperUser variable to determine further actions
if ($isSuperUser) {
	$display = "{tabulizer:data_source[8lQvfAsFFt2jD6Jq3fUxPP56]}";
} elseif ($customer_id > 0) {
	$display = "{tabulizer:data_source[wDHiyaCwklMwYpYXkquTI4jR]}";
} else {
	echo "Nothing to display!";
}

// Display the user list
echo $display;

?>