<?php

require __DIR__ . '/BreadthFirstSearch.php';

class BreadthFirstSearchTest
{
    public static function main(): void
    {
        $graph = [
            'A' => ['B', 'C'],
            'B' => ['A', 'D'],
            'D' => ['B', 'E'],
            'C' => ['A', 'E'],
            'E' => ['C', 'B', 'D'],
            'F' => [],
        ];
        var_dump(BreadthFirstSearch::search($graph, 'A', 'D'));
        var_dump(BreadthFirstSearch::search($graph, 'B', 'D'));
        var_dump(BreadthFirstSearch::search($graph, 'A', 'E'));
        var_dump(BreadthFirstSearch::search($graph, 'B', 'B'));

        print '**************************************************' . PHP_EOL;

        print_r(BreadthFirstSearch::path($graph, 'A', 'D'));
        print_r(BreadthFirstSearch::path($graph, 'A', 'E'));
        print_r(BreadthFirstSearch::path($graph, 'A', 'F'));
    }
}

BreadthFirstSearchTest::main();
