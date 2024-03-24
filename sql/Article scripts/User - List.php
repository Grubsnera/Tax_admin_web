<?php

// Script to display a list of users

// Get the current user
$user = JFactory::getUser();

// Check if the user belongs to the "Super Users" group
$superUserGroup = 8; // ID of the "Super Users" group
$isSuperUser = $user->groups && in_array($superUserGroup, $user->groups) ? true : false;

// Get the customer id
$customer_id = $_SESSION['customer_id'];

// Use the $isSuperUser variable to determine further actions
if ($isSuperUser) {
	$display = "{tabulizer:data_source[5hEQPrl1I1Q8eiNHhCAIgO3p]}";
} elseif ($customer_id > 0) {
	$customer_coded = base64_encode('1:'.$customer_id);
	$display = "{tabulizer:data_source[qFOVNFDgaazFOZA25xA8TnoL] user_params[".$customer_coded."]}";
} else {
	echo "Nothing to display!";
}

// Display the user list
echo $display;

?>