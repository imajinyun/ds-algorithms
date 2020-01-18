<?php

class BinarySearch
{
    public static function search(int $value, array $array): int
    {
        $low = 0;
        $high = count($array) - 1;

        while ($low <= $high) {
            $middle = floor(($high + $low) / 2);

            if ($array[$middle] === $value) {
                return $middle;
            }

            if ($array[$middle] > $value) {
                $high = $middle - 1;
            } else {
                $low = $middle + 1;
            }
        }

        return -1;
    }
}
