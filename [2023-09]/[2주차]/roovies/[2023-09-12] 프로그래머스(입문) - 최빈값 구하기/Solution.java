// 나의 풀이
import java.util.Arrays;
import java.util.*;

class Solution {
    public int solution(int[] array) {
        Map<Integer, Integer> map = new HashMap<>();
        int count = 0;

        for (int i = 0; i < array.length; i++) {
            if (map.get(array[i]) == null) map.put(array[i], 1);
            else {
                count = map.get(array[i]);
                map.put(array[i], count + 1);
            }
        }

        int[] distincted = Arrays.stream(array).distinct().toArray();
        count = 0;
        int answer = 0;

        for (int i = 0; i < distincted.length; i++) {
            if (map.get(distincted[i]) > count) {
                answer = distincted[i];
                count = map.get(distincted[i]);
            }
            else if (map.get(distincted[i]) == count) answer = -1;
        }

        return answer;
    }
}



// 다른 사람의 풀이
import java.util.*;
class Solution {
    public int solution(int[] array) {
        int maxCount = 0;
        int answer = 0;

        Map<Integer, Integer> map = new HashMap<>();

        // getOrDefault(Object key, V DefaultValue) : 찾는 키가 존재한다면 찾는 키의 값을 반환하고 없다면 해당 value 자료형의 기본 값을 반환하는 메서드
                // key : 값을 가져와야 하는 요소의 키
                // defaultValue : 지정된 키로 매핑된 값이 없는 경우 반환되어야 하는 기본값
        // 반환값 : 찾는 key가 존재하면 해당 key에 매핑되어 있는 값을 반환하고, 그렇지 않으면 디폴트 값이 반환

        for(int number : array) {
            int count = map.getOrDefault(number, 0) + 1;

            if(count > maxCount) {
                maxCount = count;
                answer = number;
            }

            else if(count == maxCount) {
                answer = -1;
            }

            map.put(number, count);
        }

        return answer;
    }
}