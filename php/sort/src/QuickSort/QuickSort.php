<?php

namespace Sort\QuickSort;

class QuickSort
{
    /**
     * 快速排序。
     *
     * @param array $array 待排序数组
     *
     * @return array
     */
    public static function sort(array $array): array
    {
        $count = count($array);
        if ($count < 2) {
            return $array;
        }

        [$left, $pivot, $right] = [[], $array[0], []];

        for ($i = 1; $i < $count; $i ++) {
            if ($array[$i] >= $pivot) {
                $right[] = $array[$i];
            } else {
                $left[] = $array[$i];
            }
        }

        return array_merge(self::sort($left), [$pivot], self::sort($right));
    }
}
