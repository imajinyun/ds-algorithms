<?php

require __DIR__ . '/SelectionSort.php';

class SelectionSortTest
{
    public static function main(): void
    {
        $a = SelectionSort::sort([9, 3, 5, 7, 1]);
        print_r($a);

        $b = SelectionSort::sort([10, 6, 8, 4, 2]);
        print_r($b);
    }
}

SelectionSortTest::main();
