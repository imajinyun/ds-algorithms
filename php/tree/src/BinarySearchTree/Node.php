<?php

declare(strict_types=1);

namespace Tree\BinarySearchTree;

use BadMethodCallException;

/**
 * @method Node setValue(int $value)
 * @method int getValue()
 * @method ?Node getLeftNode()
 * @method Node setLeftNode(Node $node)
 * @method ?Node getRightNode()
 * @method Node setRightNode(Node $node)
 */
class Node
{
    private int $value;
    private ?Node $left;
    private ?Node $right;

    public function __construct(int $value = 0)
    {
        $this->value = $value;
    }

    public function __call(string $name, $arguments = null)
    {
        if (preg_match('/(get)(Value|LeftNode|RightNode)$/', $name, $matches) > 0) {
            return $this->{$name};
        }

        if (preg_match('/(set)(Value|LeftNode|RightNode)$/', $name, $matches) > 0) {
            $value = $arguments[0] ?? null;
            $this->{$name} = $value;

            return $this;
        }

        throw new BadMethodCallException('调用方法不存在');
    }
}
