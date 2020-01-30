package linkedlist;

public class SinglyLinkedListMain {
    public static void main(String[] args) {
        SinglyLinkedList singlyLinkedList = new SinglyLinkedList();
        System.out.println(singlyLinkedList.isEmpty());
        System.out.println(singlyLinkedList.toString().equals(""));

        singlyLinkedList.insertToHead(1);
        singlyLinkedList.insertToHead(3);
        singlyLinkedList.insertToHead(5);
        System.out.println(singlyLinkedList.toString().equals("5->3->1"));

        singlyLinkedList.deleteToHead();
        System.out.println(singlyLinkedList.toString().equals("3->1"));

        singlyLinkedList.insertNth(5, 2);
        singlyLinkedList.insertNth(7, 2);
        System.out.println(singlyLinkedList.toString().equals("3->1->7->5"));

        singlyLinkedList.deleteNth(1);
        System.out.println(singlyLinkedList.toString().equals("3->7->5"));

        singlyLinkedList.clear();
        System.out.println(singlyLinkedList.isEmpty());

        SinglyLinkedList p = new SinglyLinkedList();
        SinglyLinkedList q = new SinglyLinkedList();

        for (int i = 10; i >= 2; i -= 2) {
            p.insertSorted(i);
            q.insertSorted(i - 1);
        }
        System.out.println(p.toString().equals("2->4->6->8->10"));
        System.out.println(q.toString().equals("1->3->5->7->9"));

        SinglyLinkedList list = SinglyLinkedList.merge(p, q);
        System.out.println(list.toString().equals("1->2->3->4->5->6->7->8->9->10"));
    }
}
