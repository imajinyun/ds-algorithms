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
    }
}
