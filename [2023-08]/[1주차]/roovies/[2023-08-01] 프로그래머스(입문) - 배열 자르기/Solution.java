import java.util.Arrays;

class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        int[] result = new int[num2 - num1 + 1];
        int j = 0;
        for (int i = num1; i <= num2; i++) {
            result[j] = numbers[i];
            j++;
        }

        return result;
    }
}


// 1줄 풀이
class Solution {
    public int[] solution(int[] numbers, int num1, int num2) {
        return Arrays.copyOfRange(numbers, num1, num2 + 1);
        // Arrays는 자바에서 배열 조작 메소드를 제공해줌
        // Arrays.copyOfRange(배열, start, end) : 주어진 배열에서 특정 범위를 새로운 배열로 복사하여 반환하는 메소드
    }
}