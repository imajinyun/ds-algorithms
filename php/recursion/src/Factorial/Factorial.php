<?php

namespace Recursion\Factorial;

class Factorial
{
    /**
     * 求给定数字的阶乘值。
     *
     * @param int $number 给定的数字
     *
     * @return int 返回 -1 表示计算失败，否则表示计算成功
     */
    public static function fact(int $number): int
    {
        if ($number < 0) {
            return -1;
        }

        if ($number === 1) {
            return $number;
        }

        return $number * self::fact($number - 1);
    }
}
