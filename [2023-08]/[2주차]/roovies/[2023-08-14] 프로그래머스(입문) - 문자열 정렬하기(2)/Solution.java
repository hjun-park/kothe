import java.util.Arrays;
import java.util.stream.*;

class Solution {
    public String solution(String my_string) {
        my_string = my_string.toLowerCase();
        return Arrays.stream(my_string.split("")).sorted().map(v -> v).collect(Collectors.joining());
    }
}

// 스트림이 아닌 Arrays 사용해서 풀이
import java.util.*;
class Solution {
    public String solution(String my_string) {
        // toCharArray()를 통해 String을 char[] 배열로 변환
        char[] c = my_string.toLowerCase().toCharArray();
        // Arrays.sort()를 이용하여 정렬 수행
        Arrays.sort(c);
        // new String()을 통해 파라미터 값을 String으로 변환하여 생성한다.
        return new String(c);
    }
}