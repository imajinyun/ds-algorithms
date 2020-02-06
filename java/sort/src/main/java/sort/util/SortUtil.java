package sort.util;

import java.util.Arrays;
import java.util.List;

final public class SortUtil {

    /**
     * 交换数组中两个键的值。
     *
     * @param array
     * @param x     数组中的前一个键名
     * @param y     数组中的后一个键名
     *
     * @return
     */
    public static boolean swap(int[] array, int x, int y) {
        int swap = array[x];
        array[x] = array[y];
        array[y] = swap;

        return true;
    }

    public static boolean compare(int x, int y) {
        return x > y;
    }

    public static void dump(int[] array) {
        System.out.println(Arrays.toString(array));
    }

    public static void dump(List<?> list) {
        System.out.println(list.toString());
    }

}
