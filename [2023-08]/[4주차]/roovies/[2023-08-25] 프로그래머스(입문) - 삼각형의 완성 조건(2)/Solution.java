// 나의 풀이
import java.util.*;

class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        Arrays.sort(sides);

        for (int i = 1; i <= sides[1]; i++) {
            if (sides[0] + i > sides[1]) answer++;
        }

        for (int i = sides[1]+1; i < sides[0] + sides[1]; i++) {
            answer++;
        }

        return answer;
    }
}

// 다른 사람의 풀이 (간단 수식)
class Solution {
    public int solution(int[] sides) {
        int answer = 0;
        int max = Math.max(sides[0], sides[1]);
        int min = Math.min(sides[0], sides[1]);

        answer += min * 2 - 1;

        return answer;
    }
}

이게 가능한 이유는 다음과 같다.
1. min * 2 : 주어진 배열 sides에서 가장 작은 변의 길이인 mim을 2번 곱한다.
            왜? 가장 작은 변의 길이를 사용하여 나머지 한 변을 만들려고 하면, 이 나머지 변의 길이는 적어도 min 보다는 커야 하기 때문이다.
            따라서 min을 두 번 곱하면서 가장 작은 변을 두 번 사용하도록 한다.
2. - 1 : 작은 변의 길이를 두 번 사용하므로서 중복되게 계산되는 부분을 제외한다.