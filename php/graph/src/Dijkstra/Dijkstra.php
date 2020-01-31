<?php

declare(strict_types=1);

namespace Graph\Dijkstra;

class Dijkstra
{
    /**
     * 已访问过的节点名称数组。
     *
     * @var array
     */
    private static $visited = [];

    /**
     * 迪克斯特拉搜索。
     *
     * 迪克斯特拉算法用于在加权图中查找最短路径，并且仅当权重为正数时才管用。
     *
     * @param array $graph 节点图数组
     * @param array $nodes 节点权重数组
     *
     * @return array
     */
    public static function search(array $graph, array $nodes): array
    {
        while ($node = self::findLowestNodeName($nodes)) {
            $value = $nodes[$node];
            $neighbors = $graph[$node];
            foreach (array_keys($neighbors) as $n) {
                $tmp = $value + $neighbors[$n];
                if ($nodes[$n] > $tmp) {
                    $nodes[$n] = $tmp;
                }
            }
            self::$visited[$node] = true;
        }

        return $nodes;
    }

    /**
     * 查找最小节点名称。
     *
     * @param array $nodes 待查找节点数组
     *
     * @return string
     */
    public static function findLowestNodeName(array $nodes): string
    {
        [$name, $lowest] = ['', PHP_INT_MAX];
        foreach ($nodes as $node => $value) {
            if ($value < $lowest && ! array_key_exists($node, self::$visited)) {
                $lowest = $value;
                $name = $node;
            }
        }

        return $name;
    }
}
