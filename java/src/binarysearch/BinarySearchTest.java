package binarysearch;

public class BinarySearchTest {
    public static void main(String[] args) {
        int[] a = {1, 3, 5, 7, 9};
        System.out.println(BinarySearch.search(3, a));

        int[] b = {2, 4, 6, 8, 10};
        System.out.println(BinarySearch.search(10, b));
    }
}
