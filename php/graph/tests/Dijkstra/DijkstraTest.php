<?php

namespace Graph\Test\Dijkstra;

use Graph\Dijkstra\Dijkstra;
use PHPUnit\Framework\TestCase;

class DijkstraTest extends TestCase
{
    private array $graph = [];
    private array $nodes = [];

    protected function setUp(): void
    {
        $this->graph = [
            'a' => ['c' => 1],
            'b' => ['a' => 3, 'c' => 5],
            'c' => [],
        ];
        $this->nodes = ['a' => 6, 'b' => 2, 'c' => PHP_INT_MAX];
    }

    public function testDijkstraSearch(): void
    {
        $expect = ['a' => 5, 'b' => 2, 'c' => 6];
        self::assertEquals($expect, Dijkstra::search($this->graph, $this->nodes));
    }

    public function testFindLowestNodeName(): void
    {
        self::assertSame('b', Dijkstra::findLowestNodeName($this->nodes));
        self::assertEquals('b', Dijkstra::findLowestNodeName($this->nodes));
    }
}
