<?php

class Node {
    public function __construct($val){
        $this->val = $val;
        $this->left = null;
        $this->right = null;
    }
}
class Solution 
{
    public function right_view(Node $node) : array {

        $queue = [$node];

        $result = [];

        while ($queue) {
            $level_size = count($queue);

            for($i = 0; $i < $level_size; $i++) {
                $node = array_shift($queue);
                if ($i == $level_size - 1) {
                    $result[] = $node->val;
                }

                if (isset($node->left)) {
                    $queue[] = $node->left;
                }

                if (isset($node->right)) {
                    $queue[] = $node->right;
                }
            }
        }

        return $result;
    }
}


$node = new Node(5);
$node->left = new Node(2);
$node->right = new Node(4);
$node->left->left = new Node(7);

$s = new Solution();
$right_view = $s->right_view($node);

echo implode("\n",$right_view);
echo "\n";

?>