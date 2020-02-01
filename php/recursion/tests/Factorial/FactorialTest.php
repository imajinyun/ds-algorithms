<?php

namespace Recursion\Test\Factorial;

use PHPUnit\Framework\TestCase;
use Recursion\Factorial\Factorial;

class FactorialTest extends TestCase
{
    public function testFact(): void
    {
        self::assertEquals(-1, Factorial::fact(-1));
        self::assertEquals(1, Factorial::fact(1));
        self::assertEquals(2, Factorial::fact(2));
        self::assertEquals(6, Factorial::fact(3));
        self::assertEquals(24, Factorial::fact(4));
        self::assertEquals(120, Factorial::fact(5));
        self::assertEquals(720, Factorial::fact(6));
        self::assertEquals(5040, Factorial::fact(7));
        self::assertEquals(40320, Factorial::fact(8));
        self::assertEquals(362880, Factorial::fact(9));
        self::assertEquals(3628800, Factorial::fact(10));
    }
}
