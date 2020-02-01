<?php

namespace Sort\SelectionSort;

class SelectionSort
{
    /**
     * 插入排序。
     *
     * @param array $array 待排序数组
     *
     * @return array
     */
    public static function sort(array $array): array
    {
        if (count($array) < 2) {
            return $array;
        }

        $result = [];
        foreach ($array as $item) {
            $index = self::findSmallestIndex($array);
            $result[] = array_splice($array, $index, 1)[0];
        }

        return $result;
    }

    /**
     * 查找最小值的索引。
     *
     * @param array $array 待排序的数组
     *
     * @return int 返回数组中最小元素的索引
     */
    public static function findSmallestIndex(array & $array): int
    {
        [$smallest, $index] = [$array[0], 0];
        foreach ($array as $key => $value) {
            if ($value < $smallest) {
                $smallest = $value;
                $index = $key;
            }
        }

        return $index;
    }
}
