package linkedlist;

public class SinglyLinkedList {
    private Node head = null;
    private int size;

    public SinglyLinkedList() {
        head = new Node(0);
        size = 0;
    }

    public SinglyLinkedList(Node head, int size) {
        this.head = head;
        this.size = size;
    }

    @Override
    public String toString() {
        if (size == 0) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        Node curr = head.next;
        while (curr != null) {
            sb.append(curr.data).append("->");
            curr = curr.next;
        }

        return sb.replace(sb.length() - 2, sb.length(), "").toString();
    }

    public void insertToHead(int data) {
        insertNth(data, 0);
    }

    public void insert(int data) {
        insertNth(data, size);
    }

    public void deleteToHead() {
        deleteNth(0);
    }

    public void delete() {
        deleteNth(size - 1);
    }

    public void insertNth(int data, int position) {
        checkBounds(position, 0, size);
        Node curr = head;

        for (int i = 0; i < position; i++) {
            curr = curr.next;
        }
        Node node = new Node(data);
        node.next = curr.next;
        curr.next = node;
        size++;
    }

    public void deleteNth(int position) {
        checkBounds(position, 0, size - 1);
        Node curr = head;
        for (int i = 0; i < position; ++i) {
            curr = curr.next;
        }

        Node node = curr.next;
        curr.next = curr.next.next;
        node = null;
        size--;
    }

    public void clear() {
        if (size == 0) {
            return;
        }

        Node prev = head.next;
        Node curr = prev.next;
        while (curr != null) {
            prev = null;
            prev = curr;
            curr = curr.next;
        }
        prev = null;
        head.next = null;
        size = 0;
    }

    /**
     * 检查边界。
     *
     * @param position
     * @param low
     * @param high
     * @throws IndexOutOfBoundsException
     */
    public void checkBounds(int position, int low, int high) {
        if (position < low || position > high) {
            throw new IndexOutOfBoundsException(position + "");
        }
    }

    public boolean isEmpty() {
        return size == 0;
    }

    public int size() {
        return size;
    }

    public class Node {
        private int data;
        private Node next;

        public Node(int data) {
            this(data, null);
        }

        public Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }

        public int getData() {
            return data;
        }
    }
}
