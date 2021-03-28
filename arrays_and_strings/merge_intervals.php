<?php

// merge intervals
class Solution
{
    public function merge_intervals($intervals) 
    {
        if (count($intervals) < 2) {
            return $intervals;
        }

        //sort intervals by start
        usort($intervals, fn($a, $b) => $a[0] - $b[0]);
        
        $start = $intervals[0][0];
        $end = $intervals[0][1];
        $output = [];

        for ($i = 1; $i < count($intervals); $i++) {
            // overlap
            if ($intervals[$i][0] <= $end) {
                $end = max($intervals[$i][1], $intervals[$i-1][1]);
            } else {
                $output[] = [$start, $end];
                $start = $intervals[$i][0];
                $end = $intervals[$i][1];
            }
        }

        $output[] = [$start, $end];

        return $output;
    }

}

$s = new Solution();
$intervals = [
    [2,5],
    [3,6],
    [15,18],
    [11,15],
    [7,10]
];

$expected = [
    [2,6],
    [7,10],
    [11,18]
];

$result = $s->merge_intervals($intervals);

foreach ($result as $interval) {
    echo "[" . implode(", ", $interval) . "]\n";
}

?>