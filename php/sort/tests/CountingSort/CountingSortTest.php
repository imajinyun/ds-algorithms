<?php

namespace Sort\Test\CountingSort;

use PHPUnit\Framework\TestCase;
use Sort\CountingSort\CountingSort;

class CountingSortTest extends TestCase
{
    public function testCountingSort(): void
    {
        $expect = [
            [1, 3, 5, 7, 9],
            [2, 4, 6, 8, 10],
            [1, 13, 17, 17, 82, 102, 433, 2390],
        ];
        $actual = [
            [9, 3, 5, 7, 1],
            [6, 10, 4, 2, 8],
            [2390, 82, 1, 17, 433, 17, 102, 13],
        ];
        foreach ($expect as $key => $item) {
            self::assertSame($item, CountingSort::sort($actual[$key]));
        }
    }
}
