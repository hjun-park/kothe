class Solution {
    public String solution(String my_string) {
        // 1. ASCII 코드값을 체크하기 위해, 128 크기를 지정함 -> 입력값이 대문자, 소문자, 공백으로 구성되어 있기 때문
        boolean[] check = new boolean[128];
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < my_string.length(); i++) {
            if (!check[my_string.charAt(i)]) { // 2. 만약 해당 문자열의 i번째 문자의 아스키코드 값이 false라면, 아직 나온적이 없는 문자임
                check[my_string.charAt(i)] = true; // 3. 따라서 해당 아스키코드 인덱스를 true로 변환한 후
                sb.append(my_string.charAt(i)); // 4. 해당 문자를 문자열에 추가함.
            }
        }
        return sb.toString();
    }
}

// 스트림 사용
import java.util.Arrays;
import java.util.stream.*;

class Solution {
    public String solution(String my_string) {
        return Arrays.stream(my_string.split("")).distinct().collect(Collectors.joining());
    }
}

