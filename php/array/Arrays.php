<?php

class Arrays
{
    /** @var array 数据 */
    private $data;

    /** @var int 容量 */
    private $capacity;

    /** @var int 长度 */
    private $length;

    /**
     * Arrays constructor.
     *
     * @param int $capacity
     */
    public function __construct(int $capacity)
    {
        if ($capacity <= 0) {
            throw new InvalidArgumentException('容量参数错误');
        }

        $this->data = [];
        $this->capacity = $capacity;
        $this->length = 0;
    }

    /**
     * 判断数组是否已满。
     *
     * @return bool
     */
    public function isFull(): bool
    {
        return $this->length === $this->capacity;
    }

    /**
     * 判断给定的索引是否超出数组范围。
     *
     * @param int $index
     *
     * @return bool
     */
    public function isOutOfRange(int $index): bool
    {
        return $index > $this->length;
    }

    /**
     * 插入值到给定的索引。
     *
     * @param int $index
     * @param int $value
     *
     * @return int 返回代码为 0 表示插入成功
     */
    public function insert(int $index, int $value): int
    {
        if ($index < 0) {
            return -1;
        }

        if ($this->isFull()) {
            return -2;
        }

        for ($i = $this->length - 1; $i >= $index; --$i) {
            $this->data[$i + 1] = $this->data[$i];
        }

        $this->data[$index] = $value;
        $this->length++;

        return 0;
    }

    /**
     * 删除给定索引的值。
     *
     * @param int $index
     *
     * @return array
     */
    public function delete(int $index): array
    {
        $value = 0;
        if ($index < 0) {
            return [-1, $value];
        }

        if ($this->isOutOfRange($index)) {
            return [-2, $value];
        }

        $value = $this->data[$index];
        for ($i = $index; $i < $this->length - 1; $i++) {
            if (isset($this->data[$i - 1])) {
                $this->data[$i] = $this->data[$i - 1];
            }
        }
        $this->length--;

        return [$index, $value];
    }

    /**
     * 查找给定索引的值。
     *
     * @param int $index
     *
     * @return array
     */
    public function find(int $index): array
    {
        $value = 0;
        if ($index < 0) {
            return [-1, $value];
        }

        if ($this->isOutOfRange($index)) {
            return [-2, $value];
        }

        return [$index, $this->data[$index]];
    }

    public function dump(): void
    {
        $format = '';
        for ($i = 0; $i < $this->length; $i++) {
            $format .= $this->data[$i] . ', ';
        }
        echo '[' . rtrim($format, ', ') . ']', PHP_EOL, PHP_EOL;
    }
}