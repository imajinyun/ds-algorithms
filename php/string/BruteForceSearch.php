<?php

class BruteForceSearch
{
    /**
     * 爆力查找。
     *
     * @param string $pattern 模式串
     * @param string $text 原始串
     *
     * @return int -1 表示匹配失败，否则表示匹配成功
     */
    public static function search(string $pattern, string $text): int
    {
        [$m, $n] = [strlen($text), strlen($pattern)];

        if ($m < $n) {
            return -1;
        }

        for ($i = 0; $i < $m - $n + 1; $i++) {
            $j = 0;
            for (; $j < $m; $j++) {
                if (isset($pattern[$i + $j]) && $pattern[$i + $j] === $text[$j]) {
                    break;
                }
            }

            if ($j === $m) {
                return $i;
            }
        }

        return $n;
    }
}
