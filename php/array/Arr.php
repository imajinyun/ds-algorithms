<?php

class Arr
{
    /** @var array 数组数据 */
    private array $data;

    /** @var int 数据容量 */
    private int $capacity;

    /** @var int 数组元素个数 */
    private int $counter;

    /**
     * Arrays constructor.
     *
     * @param int $capacity
     */
    public function __construct(int $capacity)
    {
        if ($capacity < 0) {
            throw new InvalidArgumentException('容量参数错误');
        }

        $this->data = [];
        $this->capacity = $capacity;
        $this->counter = 0;
    }

    /**
     * 插入给定索引的值。
     *
     * @param int $index
     * @param int $value
     *
     * @return bool
     */
    public function insert(int $index, int $value): bool
    {
        if ($index < 0 || $this->isOutOfRange($index)) {
            return false;
        }

        if ($this->isFull()) {
            return false;
        }

        for ($i = $this->counter; $i > $index; $i--) {
            $this->data[$i] = $this->data[$i - 1];
        }
        $this->data[$index] = $value;
        $this->counter++;

        return true;
    }

    /**
     * 删除给定索引的值。
     *
     * @param int $index
     *
     * @return bool
     */
    public function delete(int $index): bool
    {
        if ($this->isOutOfRange($index)) {
            return false;
        }

        for ($i = $index + 1; $i < $this->counter; $i++) {
            $this->data[$i - 1] = $this->data[$i];
        }
        $this->counter--;

        return true;
    }

    /**
     * 查找给定索引的值。
     *
     * @param int $index
     *
     * @return int
     */
    public function find(int $index): int
    {
        if ($index < 0 || $index >= $this->counter) {
            return -1;
        }

        return $this->data[$index];
    }

    /**
     * 判断数组是否已满。
     *
     * @return bool
     */
    private function isFull(): bool
    {
        return $this->counter === $this->capacity;
    }

    /**
     * 判断给定的索引是否超出数组范围。
     *
     * @param int $index
     *
     * @return bool
     */
    private function isOutOfRange(int $index): bool
    {
        return $index < 0 || $index > $this->counter;
    }

    /**
     * @return void
     */
    public function dump(): void
    {
        $format = '';
        for ($i = 0; $i < $this->counter; $i++) {
            $format .= $this->data[$i] . ', ';
        }
        echo '[', rtrim($format, ', '), ']', PHP_EOL;
    }
}