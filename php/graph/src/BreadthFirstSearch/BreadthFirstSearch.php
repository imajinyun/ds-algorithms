<?php

namespace Graph\BreadthFirstSearch;

class BreadthFirstSearch
{
    /**
     * 广度优先搜索。
     *
     * 广度优先搜索用于在非加权图中查找最短路径。
     *
     * @param array $graph 待搜索数组
     * @param string $start 起始节点
     * @param string $end 终止节点
     *
     * @return bool 返回 false 表示未搜索到，true 表示已搜索到
     */
    public static function search(array $graph, string $start, string $end): bool
    {
        $queue = new \SplQueue();
        $queue->enqueue($start);
        $visited = [$start];

        while (! $queue->isEmpty()) {
            $node = $queue->dequeue();

            if ($node === $end) {
                return true;
            }

            foreach ($graph[$node] as $neighbour) {
                if (! in_array($neighbour, $visited, true)) {
                    $visited[] = $neighbour;
                    $queue->enqueue($neighbour);
                }
            }
        }

        return false;
    }

    /**
     * 广度优化搜索路径。
     *
     * @param array $graph 待搜索数组
     * @param string $start 起始节点
     * @param string $end 终止节点
     *
     * @return array 返回空数组表示未搜索到合适的路径，否则表示已搜索到的合适的路径
     */
    public static function path(array $graph, string $start, string $end): array
    {
        $queue = new \SplQueue();
        $queue->enqueue([$start]); // 包装成数组入队。
        $visited = [$start];

        while (! $queue->isEmpty()) {
            $path = $queue->dequeue();
            $node = $path[sizeof($path) - 1];

            if ($node === $end) {
                return $path;
            }

            foreach ($graph[$node] as $neighbour) {
                if (! in_array($neighbour, $visited, true)) {
                    $visited[] = $neighbour;
                    $value[] = $neighbour;
                    $queue->enqueue($value);
                }
            }
        }

        return [];
    }
}
