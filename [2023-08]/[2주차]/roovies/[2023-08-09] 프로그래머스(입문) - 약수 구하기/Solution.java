import java.util.ArrayList;
import java.util.List;

class Solution {
    public int[] solution(int n) {
        List<Integer> list = new ArrayList<>();
        for(int i = 1; i <= n; i++) {
            if(n % i == 0) list.add(i);
        }
        int[] answer = new int[list.size()];
        for(int j = 0; j < answer.length; j++) {
            answer[j] = list.get(j);
        }
        return answer;
    }
}


// 스트림 사용
return IntStream.rangeClosed(1, n).filter(v -> n % v == 0).toArray();
// 📌 IntStream.rangeClosed(1, n) 을 통해 1부터 n까지의 숫자를 생성하는 IntStream을 생성한다.
// filter를 통해 n의 약수만 추려서 toArray()를 통해 배열로 반환한다.