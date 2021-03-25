<?php

// Meeting rooms
echo "[ Meeting rooms ] \n";

class Meeting 
{
    public function __construct($start, $end)
    {
        $this->start = $start;
        $this->end = $end;
    }
}

class Solution
{
    function meeting_rooms($meetings) {
        // max number of rooms 
        $max_rooms = 0;

        // sort meetings by start time
        usort($meetings, fn($a, $b) => $a->start - $b->start);

        // create heap
        $schedule = new SplMinHeap();
        
        // traverse meetings data
        foreach ($meetings as $meeting) {
            while ($schedule->count() > 1 && $schedule->top() <= $meeting->start) {
                $schedule->extract();
            }

            $schedule->insert($meeting->end);
            $max_rooms = max($max_rooms, $schedule->count());
        }

        return $max_rooms;
    }
}

// tests
$meetings_1 = array(
    new Meeting(8,9),
    new Meeting(1,5),
    new Meeting(2,6),
    new Meeting(11,12),
    new Meeting(4,5)
);

$meetings_2 = array(
    new Meeting(0,30),
    new Meeting(5,10),
    new Meeting(10,20)
);

$solution = new Solution();
$result_1 = $solution->meeting_rooms($meetings_1);
$result_2 = $solution->meeting_rooms($meetings_2);

echo "\e[1;37;42mTest 1: " . $result_1 . "\n\e[0m\n";
echo "\e[1;37;42mTest 2: " . $result_2 . "\n\e[0m\n";

?>