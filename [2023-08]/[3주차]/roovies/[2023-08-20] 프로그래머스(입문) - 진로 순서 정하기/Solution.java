// 나의 풀이
import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        int[] copied = Arrays.copyOf(emergency, emergency.length);
        int[] answer = Arrays.copyOf(emergency, emergency.length);
        Arrays.sort(copied);
        int priority = 1;
        for (int i = copied.length - 1; i >= 0; i--) {
            for (int j = 0; j < emergency.length; j++) {
                if (copied[i] == emergency[j]) {
                    answer[j] = priority;
                    priority++;
                }
            }
        }
        return answer;
    }
}

// 다른 사람 풀이 - HashMap 사용
// 📌 배열의 크기가 커질 수록 이중 반복문 보다, HashMap을 쓰는 게 더 효율적이라 한다.
import java.util.*;
class Solution {
    public int[] solution(int[] emergency) {
        Map<Integer, Integer> map = new HashMap<>();
        // 우선순위 정렬을 위해 새로운 정렬된 배열(sorted)을 선언한다.
        int[] sorted = Arrays.CopyOf(emergency, emergency.length);
        Arrays.sort(sorted);

        int size = emergency.length;
        for (int i = 0; i < sorted.length; i++) {
            map.put(sorted[i], size - i); // 오름차순으로 정렬되어 있기 때문에, 0번째에 있는 것은 가장 후순위가 되어야 하므로 size - i를 통해 우선순위를 지정함
                                          // 현재 key값으로는 배열의 원소값이 저장되어 있음
        }

        for (int i = 0; i < emergency.length; i++) {
            emergency[i] = map.get(emergency[i]); // emergency[i]에 해당하는 key값의 value(우선순위)를 가져와서 저장함.
        }
        return emergency;
    }
}