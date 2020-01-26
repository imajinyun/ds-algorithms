<?php

require __DIR__ . '/QuickSort.php';

class QuickSortTest
{
    public static function main(): void
    {
        self::dump(QuickSort::sort([5, 9, 1, 3, 7]));
        self::dump(QuickSort::sort([8, 6, 2, 4, 10]));
    }

    private static function dump(array $array): void
    {
        echo '[' . implode(', ', $array) . ']' . PHP_EOL;
    }
}

QuickSortTest::main();
