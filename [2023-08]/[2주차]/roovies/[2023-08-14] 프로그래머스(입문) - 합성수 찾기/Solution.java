class Solution {
    public int solution(int n) {
        int answer = 0;
        int count = 0;
        for (int i = 4; i <= n; i++) {
            for (int j = 1; j <= i; j++) {
                if (i % j == 0) count++;
            }
            if (count>2) {
                answer++;
                count = 0;
            }
        }
        return answer;
    }
}


// 스트림을 이용한 풀이
📌 이중 stream을 사용해야 함
import java.util.stream.IntStream;
class Solution {
    public int solution(int n) {
        return (int) IntStream.rangeClosed(1, n).filter(i -> (int) IntStream.rangeClosed(1, i).filter(j -> i % j == 0).count() > 2).count();
        // 1. IntStream.rangeClosed(1, n) : 1부터 n까지의 정수 스트림을 생성한다.
        // 2. filter()를 통해 정수 스트림 내의 요소를 필터링하는데, 이때 IntStream.rangeClosed(1, i)까지 다시 정수 스트림을 생성한 후, 거기서 다시 filter를 통해 i % j가 0인 값만 필터링하여 count()를 통해 개수를 반환한다.
        📌 이때 count()의 반환형은 long 타입을 반환하기 때문에 (int)를 통해 int형으로 변환해준다.
    }
}