<?php

namespace Sort\Support;

trait UtilTrait
{
    /**
     * 交换数组中两个键的值。
     *
     * @param array $array 待排序数组
     * @param int $x 数组中的前一个键名
     * @param int $y 数组中的后一个键名
     *
     * @return bool
     */
    final public static function swap(array & $array, int $x, int $y): bool
    {
        $tmp = $array[$y];
        $array[$y] = $array[$x];
        $array[$x] = $tmp;

        return true;
    }

    /**
     * 判断两个元素的大小。
     *
     * @param int $x
     * @param int $y
     *
     * @return int 返回 1 表示第一个元素大于第二个元素，0 表示两个元素相等，-1 表示第一个元素小于第二个元素
     */
    final public static function compare(int $x, int $y): int
    {
        return $x <=> $y;
    }
}
