<?php

namespace Sort\Test\SelectionSort;

use PHPUnit\Framework\TestCase;
use Sort\SelectionSort\SelectionSort;

class SelectionSortTest extends TestCase
{
    public function testSelectionSort(): void
    {
        $expect = [
            [1, 3, 5, 7, 9],
            [0, 1, 9, 12, 32, 78, 87, 112, 313],
        ];
        $actual = [
            [7, 9, 1, 5, 3],
            [112, 87, 313, 1, 12, 0, 9, 78, 32],
        ];
        self::assertSame($expect[0], SelectionSort::sort($actual[0]));
        self::assertSame($expect[1], SelectionSort::sort($actual[1]));
    }
}
