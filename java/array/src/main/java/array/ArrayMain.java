package array;

public class ArrayMain {
    public static void main(String[] args) {
        Array array = new Array(5);
        array.dump();
        array.insert(0, 3);
        array.insert(0, 4);
        array.insert(1, 5);
        array.insert(3, 9);
        array.insert(3, 10);
        array.insert(3, 11);
        array.dump();

        System.out.println(array.find(0));
        System.out.println(array.find(1));
        System.out.println(array.find(3));

        array.delete(3);
        array.delete(3);
        array.dump();

        System.out.println(array.find(3));
    }
}
