<?php

// Display different heading and button depending on the action
$action = JFactory::getApplication()->input->getString('action');
$description = 'country';

if ($action == 'delete') {
	$formLayout = str_replace('{header_text_message}', 'DELETE a '.$description.'!', $formLayout);
	$formLayout = str_replace('{save_button_text}', 'Delete', $formLayout);
} elseif ($action == 'edit') {
	$formLayout = str_replace('{header_text_message}', 'Edit or change a '.$description.'!', $formLayout);
	$formLayout = str_replace('{save_button_text}', 'Save', $formLayout);
} elseif ($action == 'copy') {
	$formLayout = str_replace('{header_text_message}', 'Make a copy of an existing '.$description.'!', $formLayout);
	$formLayout = str_replace('{save_button_text}', 'Copy', $formLayout);
} elseif ($action == 'add') {
	$formLayout = str_replace('{header_text_message}', 'Add a new '.$description.'!', $formLayout);
	$formLayout = str_replace('{save_button_text}', 'Add', $formLayout);
}

?>