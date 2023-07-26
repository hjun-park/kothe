class Solution {
    public int solution(int n) {
        if (n < 8) return 1;
        if (n % 7 == 0) return n / 7;
        else return (n / 7) + 1;
    }
}