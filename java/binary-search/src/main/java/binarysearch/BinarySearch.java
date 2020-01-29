package binarysearch;

public class BinarySearch {
    public static int search(int value, int[] array) {
        int low = 0;
        int high = array.length - 1;

        while (low <= high) {
            int middle = (low + high) / 2;

            if (array[middle] == value) {
                return middle;
            } else if (array[middle] > value) {
                high = middle - 1;
            } else {
                low = middle + 1;
            }
        }

        return -1;
    }
}
