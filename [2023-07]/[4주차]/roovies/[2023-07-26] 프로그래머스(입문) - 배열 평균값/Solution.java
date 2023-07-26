class Solution {
    public double solution(int[] numbers) {
        // length는 배열(Array)의 크기이며, length()는 사용되는 문자열의 길이이다.
        int sum = 0;
        for (int i = 0; i < numbers.length; i++) {
            sum += numbers[i];
        }
        return (double) sum / numbers.length;
    }
}