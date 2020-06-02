<?php

declare(strict_types=1);

namespace Tree\BinarySearchTree;

class BinarySearchTree
{
    private Node $tree;

    public function insert(int $value): void
    {
        if ($this->tree === null) {
            $this->tree = new Node($value);
            return;
        }

        $node = $this->tree;
        while ($node !== null) {
            // 待插入的值大于当前节点的值。
            if ($value > $node->getValue()) {
                if ($node->getRightNode() === null) {
                    $node->setRightNode(new Node($value));
                    return;
                }
                $node = $node->getRightNode();
            } else {
                if ($node->getLeftNode() === null) {
                    $node->setLeftNode(new Node($value));
                    return;
                }
                $node = $node->getLeftNode();
            }
        }
    }

    public function delete(int $value): void
    {
        [$curr, $prev] = [$this->tree, null];
        while ($curr !== null && $curr->getValue() !== $value) {
            $prev = $curr;
            if ($value > $prev->getValue()) {
                $curr = $curr->getRightNode();
            } else {
                $curr = $curr->getLeftNode();
            }
        }

        if ($curr === null) {
            return;
        }

        if ($curr->getLeftNode() !== null && $curr->getRightNode() !== null) {
            [$minCurrNode, $minPrevNode] = [$curr->getRightNode(), $curr];
            while ($minCurrNode->getLeftNode() !== null) {
                $minPrevNode = $minCurrNode;
                $minCurrNode = $minCurrNode->getLeftNode();
            }
            $curr->setValue($minCurrNode->getValue());
            $curr = $minCurrNode;
            $prev = $minPrevNode;
        }

        $child = null;
        if ($curr->getLeftNode() !== null) {
            $child = $curr->getLeftNode();
        } elseif ($curr->getRightNode() !== null) {
            $child = $curr->getRightNode();
        }

        if ($curr === null) {
            $this->tree = $child;
        } elseif ($prev->getLeftNode() === $curr) {
            $prev->setLeftNode($child);
        } else {
            $prev->setRightNode($child);
        }
    }
}
