import java.util.Arrays;

class Solution {
    public int solution(int order) {
        return Arrays.stream(String.valueOf(order).split("")).mapToInt(Integer::parseInt).reduce(0, (result, v) -> {
            if(v == 3 | v == 6 | v == 9) result++;
            return result;
        });
    }
}