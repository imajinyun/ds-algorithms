package org.linkedlist;

public class SinglyLinkedList {
    private Node head = null;
    private int size;

    public SinglyLinkedList() {
        head = Node(0, null);
        size = 0;
    }

    public SinglyLinkedList(Node head, int size) {
        this.head = head;
        this.next = next;
    }

    public void insertToHead(int x) {
        insertToHead(x, 0);
    }

    public void insertToHead(int data, int position) {

    }

    public static class Node {
        private int data;
        private Node next;

        public Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }

        public int getDate() {
            return data;
        }
    }
}
