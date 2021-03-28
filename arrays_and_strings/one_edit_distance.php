<?php
// one edit distance

class Solution
{
    public function one_edit_distance($str1, $str2) {

        //str1 must be shorter or equal
        if (strlen($str1) > strlen($str2)) {
            return $this->one_edit_distance($str2, $str1);
        }

        //too big of a difference?
        if (strlen($str2) - strlen($str1) > 1) {
            return false;
        }

        for ($i = 0; $i < strlen($str1); $i++) {
            if ($str1[$i] != $str2[$i]) {
                // a difference is found, remaining characters must be equal
                if (strlen($str1) == strlen($str2)) {
                    return substr($str1, $i+1) == substr($str2, $i+1);
                } else {
                    return substr($str1, $i) == substr($str2, $i+1);
                }
            } 
        }

        // both strings are equal
        return $str1 != $str2;
    }
}

$s = new Solution();

$str1 = "abababababahfhfp";
$str2 = "abababababahfhfs";

$ans = $s->one_edit_distance($str1, $str2);

var_dump($ans);

?>
