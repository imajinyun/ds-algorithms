package string;

public class BruteForceSearch {
    public static int search(String pattern, String haystack) {
        int m = pattern.length();
        int n = haystack.length();

        if (n < m) {
            return -1;
        }

        for (int i = 0; i < n - m + 1; i++) {
            int j = 0;
            for (; j < m; j++) {
                if (haystack.charAt(i + j) != pattern.charAt(j)) {
                    break;
                }
            }

            if (j == m) {
                return i;
            }
        }

        return n;
    }
}
