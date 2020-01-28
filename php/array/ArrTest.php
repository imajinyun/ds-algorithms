<?php

require __DIR__ . '/Arr.php';

class ArrTest
{
    public static function main(): void
    {
        $array = new Arr(5);
        $array->dump();

        $array->insert(0, 3);
        $array->insert(0, 4);
        $array->dump();

        $array->insert(1, 5);
        $array->insert(3, 9);
        $array->insert(3, 10);
        $array->insert(3, 11);
        $array->dump();

        var_dump($array->find(0));
        var_dump($array->find(1));
        var_dump($array->find(3));

        $array->delete(3);
        $array->dump();
        $array->delete(3);
        $array->dump();

        var_dump($array->find(3));
    }
}

ArrTest::main();
