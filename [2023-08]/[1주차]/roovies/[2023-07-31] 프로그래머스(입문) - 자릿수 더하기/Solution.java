class Solution {
    public int solution(int n) {
        String num = String.valueOf(n);
        int result = 0;
        for(int i = 0; i < num.length(); i++) {
            result += Integer.parseInt(String.valueOf(num.charAt(i)));
        }
        return result;
    }
}