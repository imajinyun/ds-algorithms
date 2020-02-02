<?php

namespace Collection\Test\Set;

use Collection\Set\SetCovering;
use Ds\Set;
use PHPUnit\Framework\TestCase;

class SetCoveringTest extends TestCase
{
    private ?Set $railways = null;
    private array $stations = [];

    protected function setUp(): void
    {
        $this->railways = new Set(['G1', 'G2', 'G3', 'G4', 'G5', 'G6', 'G7', 'G8']);
        $this->stations = [
            'zhengzhou' => new Set(['G4', 'G5', 'G6']),
            'xian' => new Set(['G1', 'G2', 'G4']),
            'lanzhou' => new Set(['G3', 'G5', 'G7']),
            'xining' => new Set(['G5', 'G6']),
            'chengdu' => new Set(['G7', 'G8']),
        ];
    }

    public function testSetCovering1(): void
    {
        $expect = ['zhengzhou', 'xian', 'lanzhou', 'chengdu'];
        $actual = SetCovering::covering($this->railways, $this->stations);
        self::assertSame($expect, $actual);
    }

    public function testSetCovering2(): void
    {
        $expect = ['one', 'two', 'thr', 'fiv'];
        $states = new Set(['mt', 'wa', 'or', 'id', 'nv', 'ut', 'ca', 'az']);
        $stations = [
            'one' => new Set(['id', 'nv', 'ut']),
            'two' => new Set(['wa', 'id', 'mt']),
            'thr' => new Set(['or', 'nv', 'ca']),
            'for' => new Set(['nv', 'ut']),
            'fiv' => new Set(['ca', 'az']),
        ];
        self::assertSame($expect, SetCovering::covering($states, $stations));
    }
}
