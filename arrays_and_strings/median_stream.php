<?php

class Solution
{
    public function __construct()
    {
        $this->above = new SplMaxHeap();
        $this->below = new SplMinHeap();
    }
    public function insert($n)
    {
        if ($this->above->count() > 0 && $n < $this->above->top()) {
            $this->above->insert($n);
        } else {
            $this->below->insert($n);
        }

        // balance heaps
        if ($this->below->count() > $this->above->count()) {
            $x = $this->below->extract();
            $this->above->insert($x);
        } 
        elseif ($this->above->count() > $this->below->count()) {
            $x = $this->above->extract();
            $this->below->insert($x);
        }
    }

    public function find_median()
    {
        if ($this->above->count() == $this->below->count()) {
            $median = ($this->above->top() + $this->below->top()) / 2;
        } elseif ($this->above->count() > $this->below->count()) {
            $median = $this->above->top();
        } else {
            $median = $this->below->top();
        }

        return $median;
    }
}

// tests
$s = new Solution();

$s->insert(3);

echo $s->find_median() == 3 ? "\e[1;37;42mpass\n\e[0m" : "\e[1;37;41mfail\n\e[0m";

$s->insert(5);
$s->insert(8);

echo $s->find_median() == 5 ? "\e[1;37;42mpass\n\e[0m" : "\e[1;37;41mfail\n\e[0m";

$s->insert(2);
$s->insert(1);

echo $s->find_median() == 3 ? "\e[1;37;42mpass\n\e[0m" : "\e[1;37;41mfail\n\e[0m";

// 1,2,3,5,8,11
$s->insert(11);
echo $s->find_median() == 4 ? "\e[1;37;42mpass\n\e[0m" : "\e[1;37;41mfail\n\e[0m";

?>