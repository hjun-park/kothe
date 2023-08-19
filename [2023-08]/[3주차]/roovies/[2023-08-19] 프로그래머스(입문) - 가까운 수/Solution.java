import java.util.*;

class Solution {
    public int solution(int[] array, int n) {
        int currentDistance = 100;
        int distance = 0;
        List<Integer> answerList = new ArrayList<>();
        for (int i = 0; i < array.length; i++) {
            distance = Math.abs(array[i] - n);
            if (distance < currentDistance) {
                answerList.clear();
                answerList.add(array[i]);
                currentDistance = distance;
            } else if (distance == currentDistance) {
                answerList.add(array[i]);
            }
        }
        Collections.sort(answerList);
        return answerList.get(0);
    }
}