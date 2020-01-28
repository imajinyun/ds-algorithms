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
     * Arr constructor.
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
        $this->counter = 0;
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
     * @param int $index 待删除元素的索引
     *
     * @return bool 返回 false 表示删除失败，否则为删除成功
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
     * @param int $index 待查找的索引
     *
     * @return int 返回 -1 表示没有找到，否则为待查找的索引指向的元素
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
     * @return bool 返回 false 表示数组未满，否则表示数组已满
     */
    private function isFull(): bool
    {
        return $this->counter === $this->capacity;
    }

    /**
     * 判断给定的索引是否超出数组范围。
     *
     * @param int $index 索引
     *
     * @return bool 返回 false 表示索引未超出数组范围，否则表示索引已超出数组范围
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
