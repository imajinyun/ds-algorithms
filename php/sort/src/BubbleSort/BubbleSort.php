<?php

namespace Sort\BubbleSort;

use Sort\Support\UtilTrait;

class BubbleSort
{
    use UtilTrait;

    /**
     * 冒泡排序。
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

        for ($i = 0; $i < $count; $i++) {
            for ($j = 0; $j < $count - 1 - $i; $j++) {
                if (self::compare($array[$j], $array[$j + 1]) > 0) {
                    self::swap($array, $j, $j + 1);
                }
            }
        }

        return $array;
    }
}
