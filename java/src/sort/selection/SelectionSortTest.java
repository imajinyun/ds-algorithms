package sort.selection;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class SelectionSortTest {
    public static void main(String[] args) {
        List<Integer> a = new ArrayList<>(Arrays.asList(5, 9, 1, 7, 3));
        System.out.println(SelectionSort.sort(a));

        List<Integer> b = new ArrayList<>(Arrays.asList(10, 6, 4, 8, 2));
        System.out.println(SelectionSort.sort(b));
    }
}
