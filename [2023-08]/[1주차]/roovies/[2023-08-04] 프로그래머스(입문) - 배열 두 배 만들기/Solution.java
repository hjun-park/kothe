class Solution {
    public int[] solution(int[] numbers) {
        for (int i = 0; i < numbers.length; i++) {
            numbers[i] *= 2;
        }
        return numbers;
    }
}


// 위 간단한 풀이를 자바8부터 지원하는 stream을 통해 다음처럼 풀 수도 있다.
// 앞으로 stream에 대해 더 공부해서 익숙해지도록 해야 한다.
import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers) {
        return Arrays.stream(numbers).map(i -> i * 2).toArray();
    }
}
// 1. Arrays.stream(배열) 을 통해 배열을 스트림으로 연다.
// 2. .map(i -> i * 2) 를 통해 스트림의 각 요소(i)에 대해 각 요소를 i * 2로 반환하여, 그 결과로 새로운 스트림을 생성한다.
// 3. 새롭게 생성된 스트림을 .toArray()를 통해 배열로 반환한다.