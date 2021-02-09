<?php

function compression($text){
    $text .= " ";
    $i = 0;
    $repeat = $text[0];
    $count = 0;
    $output = "";

    while ($i < strlen($text)) {
        if($repeat != $text[$i]) {
            $output .= $count.$repeat;
            $repeat = $text[$i];
            $count = 1;
        } else {
            $count += 1;
        }
        $i += 1;
    }

    return $output;
}

$result = compression("aaaabbbbbaaaadcfbbbbaassssssrrrrrtttvtvt");

echo $result;