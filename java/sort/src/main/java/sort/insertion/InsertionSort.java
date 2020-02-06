package sort.insertion;

import sort.util.SortUtil;

public class InsertionSort {

    public static int[] sort(int[] array) {
        if (array.length < 2) {
            return array;
        }

        for (int i = 0; i < array.length; i++) {
            for (int j = i; j > 0; j--) {
                if (SortUtil.compare(array[j - 1], array[j])) {
                    SortUtil.swap(array, j - 1, j);
                } else {
                    break;
                }
            }
        }

        return array;
    }

}
