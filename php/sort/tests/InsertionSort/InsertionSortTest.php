<?php

namespace Sort\Test\InsertionSort;

use PHPUnit\Framework\TestCase;
use Sort\InsertionSort\InsertionSort;

class InsertionSortTest extends TestCase
{
    public function testInsertionSort(): void
    {
        $expect = [
            [1, 3, 5, 7, 9],
            [2, 4, 6, 8, 10],
            [0, 1, 2, 18, 45, 98, 98, 112],
        ];
        $actual = [
            [9, 3, 5, 7, 1],
            [10, 2, 4, 8, 6],
            [112, 98, 1, 0, 18, 98, 2, 45],
        ];
        self::assertSame($expect[0], InsertionSort::sort($actual[0]));
        self::assertSame($expect[1], InsertionSort::sort($actual[1]));
        self::assertSame($expect[2], InsertionSort::sort($actual[2]));
    }
}
