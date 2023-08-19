// 스트림 사용
import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int[] solution(int n, int[] numlist) {
        // stream to Array => .toArray()
        return Arrays.stream(numlist).filter(v -> v % n == 0).toArray();
    }
}

// for문 사용
import java.util.List;
import java.util.ArrayList;

class Solution {
    public int[] solution(int n, int[] numlist) {
        List<Integer> arrlist = new ArrayList<>();
        for (int i = 0; i < numlist.length; i++) {
            if (numlist[i] % n == 0) arrlist.add(numlist[i]);
        }
        int[] result = new int[arrlist.size()];
        for (int i = 0; i < arrlist.size(); i++) {
            result[i] = arrlist.get(i);
        }
        return result;
    }
}