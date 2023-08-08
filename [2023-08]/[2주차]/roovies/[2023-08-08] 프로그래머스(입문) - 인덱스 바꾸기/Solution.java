class Solution {
    public String solution(String my_string, int num1, int num2) {
        String[] arr = my_string.split("");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if(i == num1) sb.append(arr[num2]);
            else if(i == num2) sb.append(arr[num1]);
            else sb.append(arr[i]);
        }

        return sb.toString();
    }
}

// Collections 클래스의 swap() 사용
import java.util.Arrays;
import java.util.Collections;
import java.util.List;
import java.util.stream.Collectors;

class Solution {
    public String solution(String myString, int num1, int num2) {
        // swap()은 Collections 클래스에서 지원하기 때문에, 자료형을 컬렉션으로 맞춰줘야 한다.
        // 따라서 문자열을 split을 통해 배열로 만들고, 해당 배열을 List형으로 변환해준다.
        List<String> list = Arrays.stream(myString.split("")).collect(Collectors.toList());

        // swap() 메소드를 사용하여 문자 위치를 변경해준다.
        Collections.swap(list, num1, num2);
        // String.join()을 사용하여 리스트 내의 문자들을 빈 문자열과 합쳐서 하나의 문자열로 반환한다.
        // 즉, List<String>을 String으로 변환하는 방법
        return String.join("", list);
    }
}