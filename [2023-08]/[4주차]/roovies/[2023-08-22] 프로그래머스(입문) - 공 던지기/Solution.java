class Solution {
    public int solution(int[] numbers, int k) {
        int i = 0;
        int answer = 0;
        while (true) {
            if (k==1) {
                answer = numbers[i];
                break;
            }
            k--;
            i += 2;
            if(i>numbers.length) i -= numbers.length;
        }
        return answer;
    }
}

// 다른 사람 풀이
return (k-1)*2 % numbers.length+1;
