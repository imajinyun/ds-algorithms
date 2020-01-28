<?php

class SelectionSort
{
    /**
     * 选择排序。
     *
     * @param array $array 待排序的数组。
     *
     * @return array
     */
    public static function sort(array $array): array
    {
        $result = [];
        foreach ($array as $value) {
            $index = self::findSmallestIndex($array);
            $result[] = array_splice($array, $index, 1)[0];
        }

        return $result;
    }

    /**
     * 查找最小值位置。
     *
     * @param array $array 待排序的数组
     *
     * @return int
     */
    private static function findSmallestIndex(array & $array): int
    {
        [$smallest, $index] = [$array[0], 0];

        foreach ($array as $key => $value) {
            if ($smallest > $value) {
                $smallest = $value;
                $index = $key;
            }
        }

        return $index;
    }
}
