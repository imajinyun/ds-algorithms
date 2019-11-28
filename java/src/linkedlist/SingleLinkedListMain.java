package linkedlist;

public class SingleLinkedListMain {
    public static void main(String[] args) {
        SingleLinkedList singleLinkedList = new SingleLinkedList();

        singleLinkedList.insertTail(5);
        singleLinkedList.insertToHead(2);
        singleLinkedList.insertToHead(1);
        singleLinkedList.insertTail(3);
        singleLinkedList.insertTail(1);
        singleLinkedList.dump();

        SingleLinkedList.Node a = singleLinkedList.findByIndex(0);
        System.out.println(a.getData());

        SingleLinkedList.Node b = singleLinkedList.findByIndex(2);
        System.out.println(b.getData());

        singleLinkedList.insertBefore(b, 11);
        singleLinkedList.dump();

        singleLinkedList.insertAfter(a, 22);
        singleLinkedList.dump();

        singleLinkedList.deleteByNode(a);
        singleLinkedList.dump();

        singleLinkedList.deleteByValue(11);
        singleLinkedList.dump();
    }
}
