// 나의 풀이
class Solution {
    public int solution(int i, int j, int k) {
        int count = 0;
        while(i<=j) {
            String[] str = String.valueOf(i).split("");
            for (int e = 0; e < str.length; e++) {
                if(str[e].equals(String.valueOf(k))) count++;
            }
            i++;
        }
        return count;
    }
}

// replace를 활용한 풀이
class Solution {
    public int solution(int i, int j, int k) {
        String str = "";
        for(int a = i; a <= j; a++) {
            // a+""를 통해 정수형을 문자열로 저장하게 됨 만약 i가 1이고 j가 10이면 "12345678910"이 저장됨
            str += a+"";
        }
        // 만약 k가 1이여서 1이 나온 횟수를 찾으려면
        // 전체 문자열 길이에서 1을 제외한 길이(23457890)를 빼면 1만 반복된 숫자를 얻을 수 있다.
        // 즉, 12345678910 (총 11자) - 234567890 (총 9자) = 2 (1이 2번 반복됨)
        return str.length() - str.replace(k+"", "").length();
    }
}