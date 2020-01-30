<?php

namespace LinkedList\SinglyLinkedList;

class Node
{
    public int $data;
    public ?Node $next;

    /**
     * Node constructor.
     *
     * @param int $data
     * @param Node|null $next
     */
    public function __construct(int $data = 0, Node $next = null)
    {
        $this->data = $data;
        $this->next = $next;
    }
}
