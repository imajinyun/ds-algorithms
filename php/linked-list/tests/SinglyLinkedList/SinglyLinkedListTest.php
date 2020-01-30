<?php

namespace LinkedList\Test\SinglyLinkedList;

use ArrayIterator;
use LinkedList\SinglyLinkedList\SinglyLinkedList;
use PHPUnit\Framework\TestCase;

class SinglyLinkedListTest extends TestCase
{
    private SinglyLinkedList $list;

    protected function setUp(): void
    {
        $this->list = new SinglyLinkedList();
    }

    public function testSinglyLinkedListInsertElements(): void
    {
        $this->list->insert(3);
        self::assertEquals($this->list, '3');

        $this->list->insert(7);
        self::assertEquals($this->list, '3->7');

        $this->list->insertToHead(1);
        self::assertEquals($this->list, '1->3->7');

        $this->list->insertNth(5, 2);
        self::assertEquals($this->list, '1->3->5->7');

        $this->list->insertNth(9, 4);
        self::assertEquals($this->list, '1->3->5->7->9');

        $array = [11, 13, 15, 17, 19];
        foreach ($array as $item) {
            $this->list->insert($item);
        }
        self::assertIsObject($this->list);
        self::assertInstanceOf(SinglyLinkedList::class, $this->list);
        self::assertEquals($this->list, '1->3->5->7->9->11->13->15->17->19');
    }

    public function testSinglyLinkedListDeleteElements(): void
    {
        $array = [2, 4, 6, 8, 10];
        foreach ($array as $item) {
            $this->list->insert($item);
        }
        self::assertEquals($this->list, '2->4->6->8->10');

        $this->list->delete();
        self::assertEquals($this->list, '2->4->6->8');

        $this->list->deleteToHead();
        self::assertEquals($this->list, '4->6->8');

        $this->list->deleteNth(1);
        self::assertEquals($this->list, '4->8');

        $this->list->deleteNth(0);
        $this->list->deleteNth(0);
        self::assertEquals($this->list, '');
    }

    public function testSinglyLinkedListIsEmpty(): void
    {
        self::assertIsBool($this->list->isEmpty());
        self::assertTrue($this->list->isEmpty());
    }

    public function testSinglyLinkedListSize(): void
    {
        $array = [1, 2, 3, 4, 5];
        foreach ($array as $item) {
            $this->list->insert($item);
        }
        self::assertEquals(count($array), $this->list->size());
    }
}
