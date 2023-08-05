class Solution {
    public int[] solution(int n) {
        int size = n % 2 == 0 ? n/2 : n/2 + 1;
        int[] arr = new int[size];
        int j = 0;
        for (int i = 1; i <=n; i++) {
            if (i%2 != 0) {
                arr[j] = i;
                j++;
            }
        }
        return arr;
    }
}

//위를 스트림을 통해 간결하게 표현할 수 있다.
import java.util.stream.IntStream;
class Solution {
    public int[] solution(int n) {
        return IntStream.rangeClosed(0, n).filter(value -> value % 2 == 1).toArray();
        // 1. IntStream을 통해 정수형 스트림을 생성한다.
        // 2. 이때 rangeClosed(0, n) 을 통해 0부터 n까지의 정수 스트림을 생성한다.
        // 3. filter(value -> value % 2 == 1)을 통해 정수 스트림에 있는 각각의 정수(value)가 %2 했을 때 1인 것만(홀수만) 필터링해서 남기고
        // 4. toArray() 를 통해 필터링된 스트림을 배열로 변환한다.
    }
