package sort.insertion;

import sort.util.SortUtil;

public class InsertionSortTest {

    public static void main(String[] args) {
        int[] a = {3, 9, 7, 5, 1};
        SortUtil.dump(InsertionSort.sort(a));

        int[] b = {8, 4, 10, 2, 6};
        SortUtil.dump(InsertionSort.sort(b));
    }

}
