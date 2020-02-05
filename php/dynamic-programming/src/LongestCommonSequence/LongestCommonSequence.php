<?php

declare(strict_types=1);

namespace DynamicProgramming\LongestCommonSequence;

class LongestCommonSequence
{
    /**
     * 求两个字符串的最长公共序列。
     *
     * @param string $a 字符串 a
     * @param string $b 字符串 b
     *
     * @return array
     */
    public static function search(string $a, string $b): array
    {
        [$result, $m, $n] = [[], strlen($a), strlen($b)];

        for ($i = 0; $i < $m; $i++) {
            for ($j = 0; $j < $n; $j++) {
                if ($a[$i] === $b[$j]) {
                    if (isset($result[$i - 1][$j - 1])) {
                        $result[$i][$j] = $result[$i - 1][$j - 1] + 1;
                    } else {
                        $result[$i][$j] = 1;
                    }
                } else {
                    if (isset($result[$i][$j - 1]) || isset($result[$i - 1][$j])) {
                        $result[$i][$j] = max($result[$i][$j - 1] ?? 0, $result[$i - 1][$j] ?? 0);
                    } else {
                        $result[$i][$j] = 0;
                    }
                }
            }
        }

        return $result;
    }
}
