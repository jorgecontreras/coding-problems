<?php

/*
look and say
*/

class Solution {

    public function look_and_say($string, $i, $loops) {

        // base case
        if ($i == $loops) {
            return $string;
        }

        $string .= " "; // adding dummy space to capture last sequence
        $repeat = $string[0];
        $count = 1;
        $output = "";

        for ($j = 1; $j < strlen($string); $j++) {
            if ($string[$j] == $repeat) {
                $count += 1;
            } else {
                $output .= $count . $repeat;
                $repeat = $string[$j];
                $count = 1;
            }
        }

        $i += 1;

        return $this->look_and_say($output, $i, $loops);
    }
}

$s = new Solution();
$loops = 10;
$ans = $s->look_and_say("1", 0, $loops);

echo $ans;

?>