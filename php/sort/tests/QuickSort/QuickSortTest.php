<?php

namespace Sort\Test\QuickSort;

use PHPUnit\Framework\TestCase;
use Sort\QuickSort\QuickSort;

class QuickSortTest extends TestCase
{
    public function testQuickSort(): void
    {
        self::assertEquals([2, 4, 6, 8, 10], QuickSort::sort([10, 4, 2, 8, 6]));
    }
}
