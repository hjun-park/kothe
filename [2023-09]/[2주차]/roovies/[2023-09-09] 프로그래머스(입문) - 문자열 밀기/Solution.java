import java.util.Arrays;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.stream.Collectors;

class Solution {
    public int solution(String A, String B) {
        if (A.equals(B)) return 0;


        int answer = 1;

        List<String> listA = Arrays.stream(A.split("")).collect(Collectors.toList());
        List<String> listB = Arrays.stream(B.split("")).collect(Collectors.toList());

        while (true) {
            Collections.rotate(listA, 1);
            if (listA.equals(listB)) break;
            else if (answer > listA.size()) {
                answer = -1;
                break;
            }
            else answer++;
        }

        return answer;

    }
}