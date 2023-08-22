import java.util.*;

class Solution {
    public String[] solution(String my_str, int n) {
        int idx = n;
        String[] arr = my_str.split("");
        List<String> list = new ArrayList<>();
        StringBuilder sb = new StringBuilder();

        for(int i = 0; i < arr.length; i++) {
            if(i == idx - 1 || i == arr.length-1) {
                sb.append(arr[i]);
                list.add(sb.toString());
                sb.setLength(0);
                idx += n;
            } else {
                sb.append(arr[i]);
            }
        }

        return list.toArray(new String[list.size()]);
    }
}

// 다른 사람 풀이 (스트림)
return IntStream.range(0, myStr.length() / n + (myStr.length() % n > 0 ? 1 : 0))
        .mapToObj(i -> i == myStr.length() / n ? myStr.substring(i * n) : myStr.substring(i * n, (i + 1) * n))
        .toArray(String[]::new);

1. IntStream.range(0, myStr.length() / n + (myStr.length() % n > 0 ? 1 : 0))
- IntStream.range(a, b) 를 통해 a부터 b-1 까지 정수 배열 스트림을 생성함
- 마지막 부분 문자열이 n으로 나누어 떨어지지 않는 경우를 처리하기 위해 myStr.length() / n + (myStr.length() % n > 0 ? 1 : 0) 범위를 지정


