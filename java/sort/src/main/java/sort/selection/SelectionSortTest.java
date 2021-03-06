package sort.selection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

import sort.util.SortUtil;

public class SelectionSortTest {

    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>(Arrays.asList(5, 9, 1, 7, 3));
        SortUtil.dump(SelectionSort.sort(a));

        List<Integer> b = new ArrayList<>(Arrays.asList(10, 6, 4, 8, 2));
        SortUtil.dump(SelectionSort.sort(b));
    }

}
