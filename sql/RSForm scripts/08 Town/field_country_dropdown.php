<?php

//<code>

// Build the query
$query = "
Select
    c.country_iso2 As value,
    c.country_name As label
From
    sys_country c
Group By
    c.coun_name
";

// Add a please select
$items[] = "|Please Select[c]";

// Query the database
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