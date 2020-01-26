<?php

require __DIR__ . '/Factorial.php';

class FactorialTest
{
    public static function main(): void
    {
        var_dump(Factorial::fact(-1));
        var_dump(Factorial::fact(0));
        var_dump(Factorial::fact(1));
        var_dump(Factorial::fact(2));
        var_dump(Factorial::fact(3));
        var_dump(Factorial::fact(4));
        var_dump(Factorial::fact(5));
        var_dump(Factorial::fact(6));
        var_dump(Factorial::fact(7));
        var_dump(Factorial::fact(8));
        var_dump(Factorial::fact(9));
        var_dump(Factorial::fact(10));
    }
}

FactorialTest::main();
