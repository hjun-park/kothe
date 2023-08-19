import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public String solution(String my_string) {
        // A는 아스키 코드값 65, a는 아스키 코드값 97
        // Character.toString() 메소드는 아스키값을 문자로 변환해줌
        return Arrays.stream(my_string.split("")).map(v -> v.charAt(0) > 90 ? Character.toString(v.charAt(0) - 32) : Character.toString(v.charAt(0) + 32)).collect(Collectors.joining());
    }
}