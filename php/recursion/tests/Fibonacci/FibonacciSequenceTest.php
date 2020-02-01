<?php

namespace Fibonacci\Test\Fibonacci;

use PHPUnit\Framework\TestCase;
use Recursion\Fibonacci\FibonacciSequence;

class FibonacciSequenceTest extends TestCase
{
    public function testFibonacci(): void
    {
        self::assertEquals(-1, FibonacciSequence::fibonacci(-1));
        self::assertEquals(1, FibonacciSequence::fibonacci(1));
        self::assertEquals(2, FibonacciSequence::fibonacci(2));
        self::assertEquals(3, FibonacciSequence::fibonacci(3));
        self::assertEquals(5, FibonacciSequence::fibonacci(4));
        self::assertEquals(8, FibonacciSequence::fibonacci(5));
        self::assertEquals(13, FibonacciSequence::fibonacci(6));
        self::assertEquals(21, FibonacciSequence::fibonacci(7));
        self::assertEquals(34, FibonacciSequence::fibonacci(8));
        self::assertEquals(55, FibonacciSequence::fibonacci(9));
        self::assertEquals(89, FibonacciSequence::fibonacci(10));
        self::assertEquals(144, FibonacciSequence::fibonacci(11));
        self::assertEquals(233, FibonacciSequence::fibonacci(12));
        self::assertEquals(377, FibonacciSequence::fibonacci(13));
    }
}
