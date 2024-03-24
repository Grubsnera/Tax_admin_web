<?php

// Choose the mapping profile depending on the action

if ($_POST['form']['action'] == 'add') {
    unset($mappings[1]);
    unset($mappings[2]);
} elseif ($_POST['form']['action'] == 'edit') {
    unset($mappings[0]);
    unset($mappings[2]);
} elseif ($_POST['form']['action'] == 'copy') {
    unset($mappings[1]);
    unset($mappings[2]);
} elseif ($_POST['form']['action'] == 'delete') {
    unset($mappings[0]);
    unset($mappings[1]);
} else {
    unset($mappings[0]);
    unset($mappings[1]);
    unset($mappings[2]);
}

?>