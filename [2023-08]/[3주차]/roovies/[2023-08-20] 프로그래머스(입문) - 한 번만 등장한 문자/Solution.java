// 나의 풀이
import java.util.*;
class Solution {
    public String solution(String s) {
        Map<String, Integer> map = new HashMap<>();
        String[] arr = s.split("");
        Arrays.sort(arr);

        for (int i = 0; i < arr.length; i++) {
            if (map.get(arr[i]) == null) map.put(arr[i], 1);
            else map.put(arr[i], 2);
        }
        String answer = "";
        for (int i = 0; i < arr.length; i++) {
            if (map.get(arr[i]) == 1) answer += arr[i];
        }

        return answer;
    }
}

// 다른 사람 풀이
class Solution {
    public String solution(String s) {
        // 1. 제약조건이 알파벳 소문자이므로, 알파벳을 저장할 26 크기의 배열을 선언함
        // 해당 배열을 통해 해당하는 문자의 노출 빈도를 저장할 것임
        int[] alpha = new int[26]; // 초기화가 안 되어 있으므로 기본값은 0으로 채워짐

        // 2. toCharArray()를 통해 문자열을 문자배열로 변환하여 각 문자 c를 순회함
        for(char c : s.toCharArray()){
            // 3. 이때 c - 'a'를 통해 소문자 알파벳들이 인덱스 0부터 채워질 수 있도록함.
            // 예를 들어 'h'가 온다면, 8번째 알파벳이기 때문에, h(104) - a(97) = 7이므로, 인덱스 7번의 값을 증감연산을 통해 증가시킨다.
            // 즉, 해당 문자의 빈도를 증가시키는 연산
            alpha[c - 'a']++;
        }

        StringBuilder answer = new StringBuilder();
        for(int i = 0; i < 26; i++){
            if(alpha[i] == 1){ // 4. 빈도가 1인 문자만 찾아서 문자열에 합침
                answer.append((char)(i + 'a')); // c - 'a'로 저장하였으니, i + 'a' 연산을 통해 ascii코드값을 문자열로 저장함.
            }
        }
        return answer.toString();
    }
}