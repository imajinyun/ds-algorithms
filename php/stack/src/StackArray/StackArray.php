<?php

declare(strict_types=1);

namespace Stack\StackArray;

use BadMethodCallException;
use Countable;
use InvalidArgumentException;

/**
 * @method array data()
 * @method int capacity()
 */
class StackArray implements Countable
{
    /**
     * 栈数组
     */
    private array $data;

    /**
     * 数组容量
     */
    private int $capacity;

    /**
     * 数组元素个数
     */
    private int $count;

    /**
     * StackArray constructor.
     *
     * @param int $capacity 容量
     */
    public function __construct(int $capacity)
    {
        if ($capacity < 0) {
            throw new InvalidArgumentException('容量参数错误');
        }
        $this->data = [];
        $this->capacity = $capacity;
        $this->count = 0;
    }

    /**
     * 插入给定索引的值。
     *
     * @param int $index 待插入元素的索引
     * @param int $value 待插入元素的值
     *
     * @return bool 返回 false 表示插入失败，否则为插入成功
     */
    public function insert(int $index, int $value): bool
    {
        if ($this->isOutOfRange($index)) {
            return false;
        }

        if ($this->isFull()) {
            return false;
        }

        for ($i = $this->count; $i > $index; $i--) {
            $this->data[$i] = $this->data[$i - 1];
        }
        $this->data[$index] = $value;
        $this->count++;

        return true;
    }

    /**
     * 删除给定索引的值。
     *
     * @param int $index 待删除元素的索引
     *
     * @return bool 返回 false 表示删除失败，否则为删除成功
     */
    public function delete(int $index): bool
    {
        if ($this->isOutOfRange($index)) {
            return false;
        }

        for ($i = $index + 1; $i < $this->count; $i++) {
            $this->data[$i - 1] = $this->data[$i];
        }
        $this->count--;

        return true;
    }

    /**
     * 查找给定索引的值。
     *
     * @param int $index 待查找的索引
     *
     * @return int 返回 -1 表示没有找到，否则为待查找的索引指向的元素
     */
    public function find(int $index): int
    {
        if ($this->isOutOfRange($index)) {
            return -1;
        }

        return $this->data[$index];
    }

    public function count(): int
    {
        return $this->count;
    }

    /**
     * 判断数组是否未空。
     *
     * @return bool 返回 true 表示数组为空，否则表示数组不空
     */
    public function isEmpty(): bool
    {
        return $this->count === 0;
    }

    /**
     * 判断数组是否已满。
     *
     * @return bool 返回 false 表示数组未满，否则表示数组已满
     */
    public function isFull(): bool
    {
        return $this->count === $this->capacity;
    }

    /**
     * 判断给定的索引是否超出数组范围。
     *
     * @param int $index 索引
     *
     * @return bool 返回 false 表示索引未超出数组范围，否则表示索引已超出数组范围
     */
    public function isOutOfRange(int $index): bool
    {
        return $index < 0 || $index > $this->count;
    }

    public function __call(string $name, $arguments = null)
    {
        if (preg_match('/(data|capacity)$/', $name, $matches) > 0) {
            if ($name === 'data') {
                $result = [];
                for ($i = 0; $i < $this->count(); $i++) {
                    $result[$i] = $this->data[$i];
                }
                return $result;
            } elseif ($name === 'capacity') {
                return $this->capacity;
            }
        }

        throw new BadMethodCallException('方法调用错误');
    }
}
