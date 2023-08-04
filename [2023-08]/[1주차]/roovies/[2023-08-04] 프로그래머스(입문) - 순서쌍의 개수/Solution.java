class Solution {
    public int solution(int n) {
        int count = 0;
        // i가 0부터 시작하게 된다면 ArithmeticException 에러가 발생한다.
        // ArithmeticException : 정수를 0으로 나누는 오류
        for (int i = 1; i <= n; i++) {
            if (n % i == 0) count++;
        }
        return count;
    }
}