package array;

public class Array {
    /**
     * 数组数据。
     */
    private int[] data;

    /**
     * 数组容量。
     */
    private int capacity;

    /**
     * 数组实际元素个数。
     */
    private int counter;

    public Array(int capacity) {
        if (capacity < 0) {
            System.out.println("容量参数错误");
            System.exit(-1);
        }
        this.data = new int[capacity];
        this.capacity = capacity;
        this.counter = 0;
    }

    public boolean insert(int index, int value) {
        if (isOutOfRange(index)) {
            return false;
        }

        if (isFull()) {
            return false;
        }

        for (int i = counter; i > index; i--) {
            data[i] = data[i - 1];
        }
        data[index] = value;
        counter++;

        return true;
    }

    public boolean delete(int index) {
        if (isOutOfRange(index)) {
            return false;
        }

        for (int i = index + 1; i < counter; i++) {
            data[i - 1] = data[i];
        }
        counter--;

        return true;
    }

    public int find(int index) {
        if (index < 0 || index >= counter) {
            return -1;
        }

        return data[index];
    }

    public void dump() {
        StringBuilder str = new StringBuilder();
        for (int i = 0; i < counter; i++) {
            str.append(", ").append(data[i]);
        }

        if (str.length() > 0) {
            System.out.print("[" + str.substring(2) + "]");
        } else {
            System.out.print("[" + str + "]");
        }
        System.out.println();
    }

    private boolean isOutOfRange(int index) {
        return index < 0 || index > counter;
    }

    private boolean isFull() {
        return counter == capacity;
    }
}
