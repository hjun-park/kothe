class Solution {
    public int solution(int[] box, int n) {
        int result = 1;
        for (int i = 0; i < box.length; i++) {
            result *= box[i] / n;
        }
        return result;
    }
}

// 스트림 사용 - reduce()
return Arrays.stream(box).reduce(1, (result, value) -> result * (value / n));
// reduce()는 스트림의 요소를 결헙하여 하나의 값으로 줄이는 작업을 수행한다.
// 1. Arrays.stream(box) : box배열을 스트림으로 생성한다.
// 2. 1은 초기값을 의미하며, result는 연산 중간 결과를 나타내는 변수이다. 초기값을 1로 설정했으므로, result는 1이 된다.
// 3. value는 스트림의 각 요소값을 담는 변수이다.