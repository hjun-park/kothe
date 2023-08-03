import java.util.*;

class Solution {
    public int solution(int[] sides) {
        Arrays.sort(sides);
        int op = sides[0] + sides[1];
        return sides[2] < op ? 1 : 2;
    }
}