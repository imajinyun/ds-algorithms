<?php

require __DIR__ . '/BinarySearch.php';

class BinarySearchTest
{
    public static function main(): void
    {
        var_dump(BinarySearch::search(3, [1, 2, 3, 4, 5]));
        var_dump(BinarySearch::search(10, [1, 3, 5, 7, 9]));
    }
}

BinarySearchTest::main();
