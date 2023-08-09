import java.util.Arrays;

class Solution {
    public int solution(int num, int k) {
        String[] arr = String.valueOf(num).split("");
        int result = -1;
        for(int i = 0; i < arr.length; i++) {
            if(Integer.parseInt(arr[i]) == k) {
                result = i+1;
                break;
            }
        }
        return result;
    }
}

// 한줄 풀이
return ("-" + num).indexOf(String.valueOf(k));
// 1. 인덱스를 1부터 세기 위해서 (자릿수를 물어보기 때문에 0부터 세면 안됨) 의미없는 1자리 문자열인 "-"를 넣음 (-가 아니더라도 "x", "#" 등도 상관없음)
// 2. 문자열 + 숫자 = 문자열 변환을 이용하여 "-" + num을 통해 "-123456" 같은 문자열로 만들어냄
// 3. String의 indexOf() 메소드를 이용하여 k의 인덱스 위치를 찾아냄. (이때 k는 String.valueOf() 를 통해 String으로 변환)

