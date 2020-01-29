package linkedlist2;

public class SinglyLinkedList {
    private Node head = null;

    @Override
    public String toString() {
        if (head == null) {
            return "";
        }

        StringBuilder sb = new StringBuilder();
        Node curr = head;
        while (curr != null) {
            sb.append(curr.data).append("->");
            curr = curr.next;
        }

        return sb.replace(sb.length() - 2, sb.length(), "").toString();
    }

    public void insertToHead(int value) {
        Node node = new Node(value, null);
        insertToHead(node);
    }

    public void insertToHead(Node node) {
        if (head == null) {
            head = node;
        } else {
            node.next = head;
            head = node;
        }
    }

    public void insertToTail(int value) {
        Node p = new Node(value, null);
        if (head == null) {
            head = p;
        } else {
            Node q = head;
            while (q.next != null) {
                q = q.next;
            }
            p.next = q.next;
            q.next = p;
        }
    }

    public void insertToAfter(Node node, int value) {
        Node newNode = new Node(value, null);
        insertToAfter(node, newNode);
    }

    public void insertToAfter(Node p, Node q) {
        if (p == null) {
            return;
        }

        q.next = p.next;
        p.next = q;
    }

    public void insertToBefore(Node node, int value) {
        Node newNode = new Node(value, null);
        insertToBefore(node, newNode);
    }

    public void insertToBefore(Node p, Node q) {
        if (p == null) {
            return;
        }

        if (head == p) {
            insertToHead(q);
            return;
        }

        Node curr = head;
        while (curr != null && curr.next != p) {
            curr = curr.next;
        }

        if (curr == null) {
            return;
        }

        q.next = p;
        curr.next = q;
    }

    public void deleteByNode(Node p) {
        if (p == null || head == null) {
            return;
        }

        if (p == head) {
            head = head.next;
            return;
        }

        Node q = head;
        while (q != null && q.next != p) {
            q = q.next;
        }

        if (q == null) {
            return;
        }

        q.next = q.next.next;
    }

    public void deleteByValue(int value) {
        if (head == null) {
            return;
        }

        Node p = head;
        Node q = null;
        while (p != null && p.data != value) {
            q = p;
            p = p.next;
        }

        if (p == null) {
            return;
        }

        if (q == null) {
            head = head.next;
        } else {
            q.next = q.next.next;
        }
    }

    public Node findByIndex(int index) {
        Node node = head;
        int position = 0;
        while (node != null && position != index) {
            node = node.next;
            ++position;
        }

        return node;
    }

    public Node findByValue(int value) {
        Node node = head;
        while (node != null && node.data != value) {
            node = node.next;
        }

        return node;
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
