<?php

class BreadthFirstSearch
{
    /**
     * 广度优先搜索。
     *
     * @param array $graph 待搜索数组
     * @param string $start 起始点
     * @param string $end 终止点
     *
     * @return bool 返回 false 表示没有搜索到，true 表示搜索到了
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
     * @param string $start 起始点
     * @param string $end 终止点
     *
     * @return array 返回空数组表示没有搜索到合适的路径，否则为搜索到的路径节点数组
     */
    public static function path(array $graph, string $start, string $end)
    {
        $queue = new \SplQueue();
        $queue->enqueue([$start]);
        $visited = [$start];

        while (! $queue->isEmpty()) {
            $path = $queue->dequeue();
            $node = $path[sizeof($path) - 1];

            if ($node === $end) {
                return $path;
            }

            foreach($graph[$node] as $neighbour) {
                if (!in_array($neighbour, $visited, true)) {
                    $visited[] = $neighbour;
                    $value = $path;
                    $value[] = $neighbour;
                    $queue->enqueue($value);
                }
            }
        }

        return [];
    }
}
