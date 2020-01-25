<?php

class BinarySearch
{
    /**
     * 二分查找元素在数组中的位置。
     *
     * @param int $value 待查找的元素。
     * @param array $array 待查找的数组。
     *
     * @return int -1 表示没有找到元素，否则为元素在数组中的索引。
     */
    public static function search(int $value, array $array): int
    {
        $low = 0;
        $high = count($array) - 1;

        while ($low <= $high) {
            $middle = floor(($high + $low) / 2);

            if ($array[$middle] === $value) {
                return $middle;
            }

            if ($array[$middle] > $value) {
                $high = $middle - 1;
            } else {
                $low = $middle + 1;
            }
        }

        return -1;
    }
}
