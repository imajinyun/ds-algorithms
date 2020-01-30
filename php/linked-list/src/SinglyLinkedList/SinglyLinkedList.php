<?php

namespace LinkedList\SinglyLinkedList;

class SinglyLinkedList
{
    /** @var Node 头结点 */
    private Node $head;

    /** @var int 元素个数 */
    private int $size;

    public function __construct()
    {
        $this->head = new Node();
        $this->size = 0;
    }

    public function __toString(): string
    {
        if ($this->size === 0) {
            return '';
        }
        $string = '';
        $curr = $this->head->next;
        while ($curr !== null) {
            $string .= $curr->data . '->';
            $curr = $curr->next;
        }

        return rtrim($string, '->');
    }

    public function insertToHead(int $data): void
    {
        $this->insertNth($data, 0);
    }

    public function insert(int $data): void
    {
        $this->insertNth($data, $this->size());
    }

    public function insertSorted(int $data): void
    {
        $curr = $this->head;
        while ($curr !== null && $data > $curr->next->data) {
            $curr = $curr->next;
        }

        $node = new Node($data);
        $node->next = $curr->next;
        $curr->next = $node;
        $this->size++;
    }

    public function deleteToHead(): void
    {
        $this->deleteNth(0);
    }

    public function delete(): void
    {
        $this->deleteNth($this->size() - 1);
    }

    public function insertNth(int $data, int $position): void
    {
        self::checkBounds($position, 0, $this->size());
        $curr = $this->head;

        for ($i = 0; $i < $position; $i++) {
            $curr = $curr->next;
        }

        $node = new Node($data);
        $node->next = $curr->next;
        $curr->next = $node;
        $this->size++;
    }

    public function deleteNth(int $position): void
    {
        self::checkBounds($position, 0, $this->size() - 1);
        $curr = $this->head;

        for ($i = 0; $i < $position; $i++) {
            $curr = $curr->next;
        }
        $node = $curr->next;
        $curr->next = $curr->next->next;
        $node = null;
        $this->size--;
    }

    public function clear(): void
    {
        if ($this->size() === 0) {
            return;
        }

        $prev = $this->head->next;
        $curr = $prev->next;
        while ($curr !== null) {
            $prev = null;
            $prev = $curr;
            $curr = $curr->next;
        }
        $prev = null;
        $this->head->next = null;
        $this->size = 0;
    }

    public static function merge(SinglyLinkedList $p, SinglyLinkedList $q): SinglyLinkedList
    {
        [$size, $m, $n, $head] = [
            $p->size() + $q->size(),
            $p->head->next,
            $q->head->next,
            new Node(),
        ];
        $tail = $head;

        while ($m !== null && $n !== null) {
            if ($m->data <= $n->data) {
                $tail->next = $m;
                $m = $m->next;
            } else {
                $tail->next = $n;
                $n = $n->next;
            }
            $tail = $tail->next;
        }

        if ($m === null) {
            $tail->next = $n;
        }

        if ($n === null) {
            $tail->next = $m;
        }

        return new SinglyLinkedList($head, $size);
    }

    public function isEmpty(): bool
    {
        return $this->size === 0;
    }

    public function size(): int
    {
        return $this->size;
    }

    /**
     * 检查位置边界。
     *
     * @param int $position
     * @param int $low
     * @param int $high
     *
     * @return void
     *
     * @throws \OutOfRangeException
     */
    public static function checkBounds(int $position, int $low, int $high): void
    {
        if ($position < $low || $position > $high) {
            throw new \OutOfRangeException('Index out of range');
        }
    }
}
