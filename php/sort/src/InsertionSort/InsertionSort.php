<?php

namespace Sort\InsertionSort;

use Sort\Support\UtilTrait;

class InsertionSort
{
    use UtilTrait;

    public static function sort(array $array): array
    {
        $count = count($array);
        if ($count < 2) {
            return $array;
        }

        for ($i = 0; $i < $count; $i++) {
            for ($j = $i; $j > 0; $j--) {
                if (self::compare($array[$j - 1], $array[$j]) > 0) {
                    self::swap($array, $j - 1, $j);
                } else {
                    break;
                }
            }
        }

        return $array;
    }
}
