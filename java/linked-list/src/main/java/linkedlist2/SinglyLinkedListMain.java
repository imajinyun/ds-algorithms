package linkedlist2;

public class SinglyLinkedListMain {
    public static void main(String[] args) {
        SinglyLinkedList singlyLinkedList = new SinglyLinkedList();

        int data[] = {1, 3, 5, 7, 9};
        for (int i = 0; i < data.length; i++) {
            singlyLinkedList.insertToHead(data[i]);
        }
        System.out.println(singlyLinkedList.toString().equals("9->7->5->3->1"));
        System.out.println(singlyLinkedList.findByIndex(1).getData());
        System.out.println(singlyLinkedList.findByValue(1));

        singlyLinkedList.insertToHead(11);
        System.out.println(singlyLinkedList.toString());

        singlyLinkedList.deleteByNode(singlyLinkedList.findByValue(1));
        System.out.println(singlyLinkedList.toString());

        singlyLinkedList.deleteByValue(3);
        System.out.println(singlyLinkedList.toString());
    }
}
