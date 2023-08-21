class Solution {
    public int solution(String s) {
        String[] arr = s.split(" ");
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            if (arr[i].equals("Z")) answer -= Integer.parseInt(arr[i-1]);
            else answer += Integer.parseInt(arr[i]);
        }

        return answer;
    }
}

// Stack 사용
class Solution {
    public int solution(String s) {
        int answer = 0;

        Stack<Integer> stack = new Stack<>();

        for (String a : s.split("")) {
            if (a.equals("Z")) stack.pop();
            else stack.push(Integer.parseInt(w));
        }

        for (int i : stack) {
            answer += i;
        }
        return answer;
    }
}