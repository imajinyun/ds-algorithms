package sort.bubble;

import sort.util.SortUtil;

public class BubbleSort {

    /**
     * 冒泡排序。
     *
     * @param array 待排序数组
     *
     * @return 返回排序数组
     */
    public static int[] sort(int[] array) {
        if (array.length < 2) {
            return array;
        }

        for (int i = 0; i < array.length; i++) {
            for (int j = 0; j < array.length - 1 - i; j++) {
                if (SortUtil.compare(array[j], array[j + 1])) {
                    SortUtil.swap(array, j, j + 1);
                }
            }
        }

        return array;
    }

}
