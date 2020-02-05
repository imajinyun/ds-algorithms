<?php

namespace Sort\CountingSort;

use SplFixedArray;

class CountingSort
{
    /**
     * 计数排序。
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

        // 保证数组的最后一个索引为 max
        $max = self::findLargestValue($array) + 1;

        // 数组 $bucket 键对应的值记录的值是 $array 中某元素出现的次数。
        $bucket = (new SplFixedArray($max));
        foreach ($array as $key => $val) {
            $value = $bucket->offsetGet($array[$key]) + 1;
            $bucket->offsetSet($array[$key], $value);
        }

        $index = 0;
        for ($i = 0; $i < $max; $i++) {
            while ($bucket[$i] > 0) {
                $array[$index++] = $i;
                $bucket->offsetSet($i, $bucket->offsetGet($i) - 1);
            }
        }

        return $array;
    }

    /**
     * 查找数组中的最大值。
     *
     * @param array $array 待查找数组
     *
     * @return int 返回数组中的最大值
     */
    private static function findLargestValue(array $array): int
    {
        $max = $array[0];
        foreach ($array as $value) {
            if ($value > $max) {
                $max = $value;
            }
        }

        return $max;
    }
}
