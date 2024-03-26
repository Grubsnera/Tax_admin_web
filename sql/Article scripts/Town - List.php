<?php

if ($_SERVER["REQUEST_METHOD"] == "POST") {

    // Get the town name
    $TownName = isset($_POST['town_name']) ? $_POST['town_name'] : "";

    // If a town name was given
    if ($TownName) {

        // echo "User's answer is: " . $TownName;

        // Get the current user
        $user = JFactory::getUser();

        // Check if the user belongs to the "Super Users" group
        $superUserGroup = 8; // ID of the "Super Users" group
        $isSuperUser = $user->groups && in_array($superUserGroup, $user->groups) ? true : false;

        // Get the customer id
        $customer_id = $_SESSION['customer_id'];

        // Use the $isSuperUser variable to determine further actions
        $town_coded = base64_encode('1:'.$TownName);
        if ($isSuperUser) {
            $display = "{tabulizer:data_source[jN2ZvXrnf1ogGwT1M2LNtP5r] user_params[".$town_coded."]}";
        } elseif ($customer_id > 0) {
            $display = "{tabulizer:data_source[BD1invaIRZJP90io9cP4375l] user_params[".$town_coded."]}";
        } else {
            // echo "Nothing to display!";
            $display = "No towns found to display!";
        }

        // Display the user list
        echo $display;

    } else {

        echo "No towns found to display!";

    }

}

?>