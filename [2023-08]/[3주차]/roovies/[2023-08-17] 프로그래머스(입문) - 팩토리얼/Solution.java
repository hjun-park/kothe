class Solution {
    public int solution(int n) {
        int result = 0;
        int i = 1;
        while (true) {
            result = recursive(i);
            if(result > n) {
                return i - 1;
            } else {
                i++;
                continue;
            }
        }
    }

    private int recursive(int n) {
        return n > 1 ? n * recursive(n-1) : n;
    }
}