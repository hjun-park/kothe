// 나의 풀이
class Solution {
    public String[] solution(String[] quiz) {
        String[] answer = new String[quiz.length];

        for (int i = 0; i < quiz.length; i++) {
            String[] exp = quiz[i].split(" ");
            int result = 0;
            if (exp[1].equals("+")) result = Integer.parseInt(exp[0]) + Integer.parseInt(exp[2]);
            else if (exp[1].equals("-")) result = Integer.parseInt(exp[0]) - Integer.parseInt(exp[2]);

            answer[i] = result == Integer.parseInt(exp[4]) ? "O" : "X";
        }

        return answer;
    }
}

// 다른 사람의 풀이
class Solution {
    public String[] solution(String[] quiz) {
        for(int i=0; i<quiz.length; i++){
            String[] text = quiz[i].split(" ");
            int result = Integer.parseInt(text[0]) + ( Integer.parseInt(text[2]) * ( text[1].equals("+") ? 1:-1) );
            quiz[i] = result == Integer.parseInt(text[4])? "O": "X";
        }
        return quiz;
    }
}