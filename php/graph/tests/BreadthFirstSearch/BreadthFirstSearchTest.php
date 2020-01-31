<?php

namespace Graph\Test\BreadthFirstSearch;

use Graph\BreadthFirstSearch\BreadthFirstSearch;
use PHPUnit\Framework\TestCase;

class BreadthFirstSearchTest extends TestCase
{
    private array $graph = [];

    protected function setUp(): void
    {
        $this->graph = [
            'A' => ['B', 'C'],
            'B' => ['A', 'D'],
            'D' => ['B', 'E'],
            'C' => ['A', 'E'],
            'E' => ['C', 'B', 'D'],
            'F' => [],
        ];
    }

    public function testBreadthFirstSearch(): void
    {
        self::assertTrue(BreadthFirstSearch::search($this->graph, 'A', 'D'));
        self::assertTrue(BreadthFirstSearch::search($this->graph, 'B', 'D'));
        self::assertTrue(BreadthFirstSearch::search($this->graph, 'A', 'E'));
        self::assertTrue(BreadthFirstSearch::search($this->graph, 'B', 'B'));
        self::assertFalse(BreadthFirstSearch::search($this->graph, 'F', 'E'));
        self::assertFalse(BreadthFirstSearch::search($this->graph, 'E', 'F'));
        self::assertFalse(BreadthFirstSearch::search($this->graph, 'A', 'F'));
    }

    public function testBreadthFirstSearchPath(): void
    {
        self::assertIsArray(BreadthFirstSearch::path($this->graph, 'A', 'D'));
        self::assertEquals(BreadthFirstSearch::path($this->graph, 'A', 'D'), ['B', 'C', 'D']);
        self::assertEquals(BreadthFirstSearch::path($this->graph, 'A', 'E'), ['B', 'C', 'D', 'E']);
        self::assertEquals(BreadthFirstSearch::path($this->graph, 'A', 'F'), []);
        self::assertEquals(BreadthFirstSearch::path($this->graph, 'E', 'F'), []);
    }
}
