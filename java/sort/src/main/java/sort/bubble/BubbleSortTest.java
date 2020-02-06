package sort.bubble;

import sort.util.SortUtil;

public class BubbleSortTest {

    public static void main(String[] args) {
        int[] a = {9, 7, 3, 1, 5};
        SortUtil.dump(BubbleSort.sort(a));

        int[] b = {10, 8, 2, 4, 6};
        SortUtil.dump(BubbleSort.sort(b));
    }

}
