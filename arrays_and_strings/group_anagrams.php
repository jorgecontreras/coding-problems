<?php

/*
group anagrams
*/

class Solution 
{
    public function group_anagrams($words) {
        $groups = array();

        foreach ($words as $word) {
            $chars = str_split($word);
            sort($chars);
            $key = implode($chars);

            if(!isset($groups[$key])) {
                $groups[$key] = array();
            }
            $groups[$key][] = $word;
        }

        return $groups;

    }
}

$words = ["cab","cod","tin","pew","duh","may","ill","buy","int","bar","max","doc", "nit", "same", "mase", "ames"];

$s = new Solution();
$anagrams = $s->group_anagrams($words);

foreach ($anagrams as $key => $words) {
    echo $key . ": [";
    echo implode(", ", $words);
    echo "]\n";
}

?>