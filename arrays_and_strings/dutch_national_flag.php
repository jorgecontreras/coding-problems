<?php

/*
Dutch national flag
*/

class Solution
{
    public function dnf($nums) {
        $left = 0;
        $right = count($nums) - 1;
        $i = 0;

        while ($i <= $right) {
            if ($nums[$i] == 0) {
                $nums[$i] = $nums[$left];
                $nums[$left] = 0;
                $left += 1;
                $i += 1;
            }
            elseif ($nums[$i] == 2) {
                $nums[$i] = $nums[$right];
                $nums[$right] = 2;
                $right -= 1;
            } else {
                $i += 1;
            }
        }
        
        return $nums;
    }
}


$s = new Solution();

$nums = [2, 1, 2, 0, 0, 2, 1, 0, 1, 0, 0, 2, 2, 2, 1, 2, 0, 0, 0, 2, 1, 0, 2, 0, 0, 1];
$sorted = $s->dnf($nums);

echo implode(", ", $sorted);

?>