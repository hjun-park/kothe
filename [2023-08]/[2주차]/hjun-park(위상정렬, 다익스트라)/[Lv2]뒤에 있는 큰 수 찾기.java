import java.util.ArrayDeque;
import java.util.Deque;

class Solution {
    public int[] solution(int[] numbers) {
        int[] answer = new int[numbers.length];
		Deque<Integer> s = new ArrayDeque<>();

		for(int i=numbers.length-1; i>=0; i--){
			while(!s.isEmpty()){
				if(s.peek() > numbers[i]){
					answer[i] = s.peek();
					break;
				}else{
					s.pop();
				}
			}
			if(s.isEmpty()){
				answer[i] = -1;
			}
			s.push(numbers[i]);
		}


        return answer;
    }
}
