<?php

namespace Search\Test\BinarySearch;

use PHPUnit\Framework\TestCase;
use Search\BinarySearch\BinarySearch;

class BinarySearchTest extends TestCase
{
    public function testBinarySearch(): void
    {
        self::assertEquals(2, BinarySearch::search(3, [1, 2, 3, 4, 5]));
        self::assertEquals(-1, BinarySearch::search(10, [1, 3, 5, 7, 9]));
        self::assertEquals(0, BinarySearch::search(4, [4, 4, 5, 6, 7, 8]));
    }
}
