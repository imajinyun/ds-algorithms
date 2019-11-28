package linkedlist;

public class SingleLinkedList {
    private Node head = null;

    public Node findByValue(int value) {
        Node p = head;
        while (p != null && p.data != value) {
            p = p.next;
        }

        return p;
    }

    public Node findByIndex(int index) {
        Node p = head;
        int pos = 0;
        while (p != null && pos != index) {
            p = p.next;
            pos++;
        }

        return p;
    }

    public void insertToHead(int value) {
        Node node = new Node(value, null);
        insertToHead(node);
    }

    public void insertToHead(Node node) {
        if (null == head) {
            head = node;
        } else {
            node.next = head;
            head = node;
        }
    }

    public void insertTail(int value) {
        Node node = new Node(value, null);
        if (null == head) {
            head = node;
        } else {
            Node q = head;
            while (q.next != null) {
                q = q.next;
            }
            node.next = q.next;
            q.next = node;
        }
    }

    public void insertAfter(Node p, int value) {
        Node node = new Node(value, null);
        insertAfter(p, node);
    }

    public void insertAfter(Node p, Node q) {
        if (p == null) {
            return;
        }
        q.next = p.next;
        p.next = q;
    }

    public void insertBefore(Node p, int value) {
        Node node = new Node(value, null);
        insertBefore(p, node);
    }

    public void insertBefore(Node p, Node q) {
        if (p == null) {
            return;
        }

        if (p == head) {
            insertToHead(q);
            return;
        }

        Node node = head;
        while (node != null && node.next != p) {
            node = node.next;
        }

        if (node == null) {
            return;
        }

        q.next = p;
        node.next = q;
    }

    public void deleteByNode(Node node) {
        if (node == null || head == null) {
            return;
        }

        if (node == head) {
            head = head.next;
            return;
        }

        Node q = head;
        while (q != null && q.next != node) {
            q = q.next;
        }

        if (q == null) {
            return;
        }
        q.next = q.next.next;
    }

    public void deleteByValue(int value) {
        if (null == head) {
            return;
        }

        Node p = head;
        Node q = null;

        while (null != p && p.data != value) {
            q = p;
            p = p.next;
        }

        if (null == p) {
            return;
        }

        if (null == q) {
            head = head.next;
        } else {
            q.next = q.next.next;
        }
    }

    public void dump() {
        Node node = head;
        while (null != node) {
            System.out.print(node.data + " ");
            node = node.next;
        }
        System.out.println();
    }

    public static class Node {
        private int data;
        private Node next;

        public Node(int data, Node next) {
            this.data = data;
            this.next = next;
        }

        public int getData() {
            return data;
        }
    }
}
