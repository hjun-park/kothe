// 나의 풀이
import java.util.*;
class Solution {
    public int[] solution(int[][] score) {
        // 자꾸 테스트 케이스 3, 6이 오류가 나서 질문하기를 찾아보니 double형으로 변환해야 했다.
        // 나눌 때 2.0으로 나눴어야 함
        double[] avgs = new double[score.length];
        for (int i = 0; i < score.length; i++) {
            avgs[i] = (score[i][0] + score[i][1]) / 2.0;
        }
        double[] sorted = Arrays.stream(avgs).sorted().toArray();

        Map<Double, Integer> map = new HashMap<>();
        int rank = 1;
        for (int i = sorted.length - 1; i  >= 0; i--) {
            if (map.get(sorted[i]) != null) {
                rank++;
                continue;
            }
            map.put(sorted[i], rank);
            rank++;
        }

        List<Integer> list = new ArrayList<>();

        for (int i = 0; i < avgs.length; i++) {
            list.add(map.get(avgs[i]));
        }

        int[] answer = list.stream().mapToInt(i -> i).toArray();

        return answer;
    }
}

// 다른 사람의 풀이
import java.util.*;
class Solution {
    public int[] solution(int[][] score) {
        // 점수 순위를 저장할 List 선언
        List<Integer> scoreList = new ArrayList<>();
        for(int[] t : score){
            // 어차피 ÷2를 안 해도, 합계를 기준으로 순서를 정할 수 있음.
            // 따라서 굳이 ÷2를 해서 double형으로 계산할 필요 없이 합계로 계산하여 int형 그대로 사용할 수 있게 함
            scoreList.add(t[0] + t[1]);
        }
        // Comparator.reverseOrder()를 사용하여 내림차순으로 정렬하도록 함.
        scoreList.sort(Comparator.reverseOrder());

        // 점수를 가지고 있는 score.length만큼 배열 선언
        int[] answer = new int[score.length];
        for(int i=0; i<score.length; i++){
            // indexOf를 사용하여 합계의 순위를 지정함
            // 이때 차후에 중복된 값이 나오더라도, 💡indexOf는 가장 작은 index 위치를 반환하기 때문💡에 상관없음.
            answer[i] = scoreList.indexOf(score[i][0] + score[i][1])+1;
        }
        return answer;
    }
}
