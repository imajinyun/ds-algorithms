<?php

require __DIR__ . '/FibonacciSequence.php';

class FibonacciSequenceTest
{
    public static function main(): void
    {
        var_dump(FibonacciSequence::fibonacci(-1));
        var_dump(FibonacciSequence::fibonacci(0));
        var_dump(FibonacciSequence::fibonacci(1));
        var_dump(FibonacciSequence::fibonacci(2));
        var_dump(FibonacciSequence::fibonacci(3));
        var_dump(FibonacciSequence::fibonacci(4));
        var_dump(FibonacciSequence::fibonacci(5));
        var_dump(FibonacciSequence::fibonacci(6));
        var_dump(FibonacciSequence::fibonacci(7));
        var_dump(FibonacciSequence::fibonacci(8));
        var_dump(FibonacciSequence::fibonacci(9));
        var_dump(FibonacciSequence::fibonacci(10));
    }
}

FibonacciSequenceTest::main();
