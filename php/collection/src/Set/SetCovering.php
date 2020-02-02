<?php

namespace Collection\Set;

use Ds\Set;

class SetCovering
{
    /**
     * 贪婪算法计算最小覆盖集合。
     *
     * @param \Ds\Set $sets 全部元素的集合
     * @param array $array 覆盖元素的集合
     *
     * @see http://docs.php.net/manual/en/book.ds.php
     *
     * @return array 返回最小覆盖集合元素数组
     */
    public static function covering(Set $set, array $array): array
    {
        $resultSet = new Set();
        while (! $set->isEmpty()) {
            [$newElement, $newCoveredSet] = [null, new Set()];
            foreach (array_keys($array) as $value) {
                [$tmpNodeSet, $tmpCoveredSet] = [$array[$value], new Set($set)];
                $tmpCoveredSet = $tmpCoveredSet->filter(function ($value) use ($tmpNodeSet) {
                    return $tmpNodeSet->contains($value);
                });

                if ($tmpCoveredSet->count() > $newCoveredSet->count()) {
                    $newElement= $value;
                    $newCoveredSet = $tmpCoveredSet;
                }
            }
            $resultSet->add($newElement);

            $set = new Set($set);
            $set = $set->filter(function ($value) use ($newCoveredSet) {
                return ! $newCoveredSet->contains($value);
            });
        }

        return $resultSet->toArray();
    }
}
