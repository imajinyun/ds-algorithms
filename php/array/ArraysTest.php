<?php

require __DIR__ . '/Arrays.php';

class ArraysTest
{
    public static function main(): void
    {
        $array = new Arrays(10);

        for ($i = 0; $i < 9; $i++) {
            $array->insert($i, $i * 2);
        }
        $array->dump();

        if (0 === $code = $array->insert(5, 55)) {
            echo '插入成功', PHP_EOL;
        } else {
            echo '插入失败', PHP_EOL;
        }
        $array->dump();

        [$index, $value] = $array->delete(5);
        echo $index, ' ', $value, PHP_EOL;
        $array->dump();

        if (0 === $code = $array->insert(11, 11)) {
            echo '插入成功', PHP_EOL;
        } else {
            echo '插入失败', PHP_EOL;
        }
        $array->dump();

        [$index, $value] = $array->find(11);
        echo $index, ' ', $value, PHP_EOL;
        $array->dump();

        [$index, $value] = $array->delete(0);
        echo $index, ' ', $value, PHP_EOL;
        $array->dump();

        [$index, $value] = $array->find(0);
        echo $index, ' ', $value, PHP_EOL;
        $array->dump();
    }
}

ArraysTest::main();