<?php

class FibonacciSequence
{
    /**
     * 求给定数字的斐波那契数列值。
     *
     * @param int $number 给定的数字
     *
     * @return int 返回 -1 表示计算失败，否则表示计算成功
     */
    public static function fibonacci(int $number): int
    {
        if ($number < 0) {
            return -1;
        }

        if ($number === 0 || $number === 1) {
            return $number;
        }

        return self::fibonacci($number - 1) + self::fibonacci($number - 2);
    }
}
