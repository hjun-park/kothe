class Solution {
    public String solution(String my_string, int n) {
        String[] arr = my_string.split("");
        String answer = "";
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < n; j++) {
                answer += arr[i];
            }
        }
        return answer;
    }
}

// String의 repeat() 메소드를 사용하면 좋다.
// repeat() 메소드는 자바11에 새로 추가된 String 메소드이다.