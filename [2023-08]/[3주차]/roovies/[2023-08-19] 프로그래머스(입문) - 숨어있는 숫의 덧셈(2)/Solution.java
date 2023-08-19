//정답
class Solution {
    public int solution(String my_string) {
        String[] arr = my_string.split("[a-zA-Z]");
        // 정규표현식을 사용하여, 알파벳 기준으로 분할한다.
        int answer = 0;
        for (int i = 0; i < arr.length; i++) {
            answer += !arr[i].isEmpty() ? Integer.parseInt(arr[i]) : 0; // 값이 있으면 더하는데, 없으면 0을 반환해야 하기 때문에 문자열이 비어있으면 0을 더하도록 한다.
        }
        return answer;
    }
}

//나의 풀이
// 내가 생각한 알고리즘
// 1. 당시에 split()에 정규표현식을 사용할 수 있다는 것을 몰랐다.
// 2. 따라서 replaceAll을 통해, 정규표현식에서 +를 사용하면 연속되는 것을 의미하기 때문에 자연수를 제외한 모든 대소문자를 a로 변환해줬다.
// 3. 그리고 for문을 돌며, a가 아닐 경우는 숫자이므로 value에 추가한 후, a가 나오게 되면 value에 저장된 값까지 자연수이기 떄문에 정수로 변환하여 저장해줬다.
// 4. 이때 만약 문자열 내에 정수가 존재하지 않는다면 0을 반환해야 하기 때문에 value를 "0"으로 두었다.
// 위 과정을 생각하여 아래 코드를 작성하였는데, 10개의 테스트 중 2~7번 테스트에 실패했다.
class Solution {
    public int solution(String my_string) {
        my_string = my_string.replaceAll("[^0-9]+", "a");
        // 정규표현식에서 '+'는 1번 이상을 의미한다.
        // 따라서 위 정규표현식을 풀어 쓰면 0-9가 아닌 문자열 중에 +로 1번 이상 반복되는 것을 다 a로 치환한다는 것.
        int answer = 0;
        String value = "0";
        String[] arr = my_string.split("");
        for (int i = 0; i < arr.length; i++) {
            if(!arr[i].equals("a")) {
                value += arr[i];
            } else {
                answer += Integer.parseInt(value);
                value = "0";
            }
        }
        return answer;
    }
}