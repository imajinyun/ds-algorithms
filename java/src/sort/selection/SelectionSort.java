package sort.selection;

import java.util.ArrayList;
import java.util.List;

public class SelectionSort {
    public static List<Integer> sort(List<Integer> array) {
        List<Integer> result = new ArrayList<>();

        int size = array.size();
        for (int i = 0; i < size; i++) {
            int index = findSmallestIndex(array);
            result.add(array.get(index));
            array.remove(index);
        }

        return result;
    }

    /**
     * 查找最小元素位置索引。
     *
     * @param array
     * @return index 返回 -1 表示查找失败，否则表示元素在数组中的位置索引。
     */
    private static int findSmallestIndex(List<Integer> array) {
        int smallest = array.get(0), index = 0;
        for (int i = 0; i < array.size(); i++) {
            if (array.get(i) < smallest) {
                smallest = array.get(i);
                index = i;
            }
        }

        return index;
    }
}
