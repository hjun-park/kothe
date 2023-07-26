class Solution {
    public int solution(int num1, int num2) {
        double divided = (double) num1 / num2;
        int result = (int) (divided * 1000);
        return result;
    }
}