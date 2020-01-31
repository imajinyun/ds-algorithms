<?php

namespace Sort\Test\BubbleSort;

use PHPUnit\Framework\TestCase;
use Sort\BubbleSort\BubbleSort;

class BubbleSortTest extends TestCase
{
    public function testBubbleSort(): void
    {
        self::assertEquals([1, 3, 5, 7, 9], BubbleSort::sort([9, 3, 5, 1, 7]));
    }
}
