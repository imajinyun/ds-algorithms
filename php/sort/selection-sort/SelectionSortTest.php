<?php

require __DIR__ . '/SelectionSort.php';

class SelectionSortTest
{
    public static function main(): void
    {
        self::dump(SelectionSort::sort([9, 3, 5, 7, 1]));
        self::dump(SelectionSort::sort([10, 6, 8, 4, 2]));
    }

    private static function dump(array $array): void
    {
        echo '[' . implode(', ', $array) . ']' . PHP_EOL;
    }
}

SelectionSortTest::main();
