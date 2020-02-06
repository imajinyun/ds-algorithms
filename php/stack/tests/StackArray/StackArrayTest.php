<?php

declare(strict_types=1);

namespace Stack\Test\StackArray;

use OutOfRangeException;
use PHPUnit\Framework\TestCase;
use Stack\StackArray\StackArray;

class StackArrayTest extends TestCase
{
    private StackArray $stack;

    protected function setUp(): void
    {
        $this->stack = new StackArray(5);
    }

    public function testInsert(): void
    {
        self::assertEquals(5, $this->stack->capacity());
        self::assertCount(0, $this->stack);

        self::assertTrue($this->stack->insert(0, 3));
        self::assertTrue($this->stack->insert(0, 4));
        self::assertSame([4, 3], $this->stack->data());
        self::assertCount(2, $this->stack);

        self::assertTrue($this->stack->insert(1, 5));
        self::assertSame([4, 5, 3], $this->stack->data());
        self::assertCount(3, $this->stack);

        self::assertTrue($this->stack->insert(3, 10));
        self::assertSame([4, 5, 3, 10], $this->stack->data());
        self::assertCount(4, $this->stack);

        self::assertTrue($this->stack->insert(3, 11));
        self::assertSame([4, 5, 3, 11, 10], $this->stack->data());

        self::assertFalse($this->stack->insert(0, 100));
        self::assertCount(5, $this->stack);
    }

    public function testDelete(): void
    {
        foreach ([1, 2, 3, 4, 5] as $key => $value) {
            $this->stack->insert($key, $value);
        }
        self::assertSame([1, 2, 3, 4, 5], $this->stack->data());
        self::assertTrue($this->stack->delete(4));
        self::assertCount(4, $this->stack);
        self::assertSame([1, 2, 3, 4], $this->stack->data());

        self::assertTrue($this->stack->delete(3));
        self::assertSame([1, 2, 3], $this->stack->data());

        self::assertTrue($this->stack->delete(2));
        self::assertSame([1, 2], $this->stack->data());

        self::assertTrue($this->stack->delete(1));
        self::assertSame([1], $this->stack->data());

        self::assertTrue($this->stack->delete(0));
        self::assertSame([], $this->stack->data());
        self::assertEquals(-1, $this->stack->find(4));
        self::assertCount(0, $this->stack);
    }

    public function testFind(): void
    {
        $this->stack->insert(0, 1);
        self::assertSame(1, $this->stack->find(0));

        $this->stack->insert(1, 2);
        self::assertSame(2, $this->stack->find(1));

        $this->stack->insert(2, 3);
        self::assertSame(3, $this->stack->find(2));

        self::assertSame([1, 2, 3], $this->stack->data());
        self::assertCount(3, $this->stack);
        self::assertEquals(5, $this->stack->capacity());
    }

    public function testIsEmpty(): void
    {
        self::assertEmpty($this->stack);
        self::assertTrue($this->stack->isEmpty());
    }

    public function testIsFull(): void
    {
        foreach ([1, 3, 5, 7, 9] as $value) {
            $this->stack->insert(0, $value);
        }
        self::assertCount(5, $this->stack);
        self::assertTrue($this->stack->isFull());
    }

    public function testIsOutOfRange(): void
    {
        self::assertTrue($this->stack->isOutOfRange(-1));
        self::assertFalse($this->stack->isOutOfRange(0));
        self::assertTrue($this->stack->isOutOfRange(1));
        self::assertTrue($this->stack->isOutOfRange(4));
        self::assertTrue($this->stack->isOutOfRange(6));
    }
}
