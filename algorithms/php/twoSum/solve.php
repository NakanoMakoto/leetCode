<?php
class Solution {
	/**
	 * @param Integer[] $nums
	 * @param Integer $target
	 * @return Integer[]
	 */
	function twoSum($nums, $target) {
        for ($i = 0; $i < count($nums); $i++) {
            for ($j = 0; $j < count($nums); $j++) {
                if($j === $i) {
                    continue;
                }
                if ($nums[$j] === $target - $nums[$i]) {
                    return [$i, $j];
                }
            }
        }
    }
}
