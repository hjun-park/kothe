class Solution {
    public int solution(int n) {
        int answer = 0;
        for(int i = 0; i < n; i++) {
            answer++;
            while(answer % 3 == 0 || String.valueOf(answer).contains("3")) answer++;
        }

        return answer;
    }
}

// 어차피 i -> n 까지 차근차근 수를 세기 때문에,
// answer도 같이 증가시켜주면서, 3의 배수거나, 3을 포함하고 있는지 검사하여 추가적으로 증가시켜주면 된다.