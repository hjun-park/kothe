import java.util.*;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        int i = 2;
        while(i<=n) {
            if (n % i == 0) { // n % i == 0을 통해 4, 6, 8 같은 수를 신경쓰지 않아도 됨. 자동으로 최소의 수로 나눠지기 때문
                list.add(i);
                n = n / i;
            }
            else {
                i++;
                continue;
            }
        }
        return list.stream().distinct().sorted().mapToInt(v -> v).toArray();
    }
}