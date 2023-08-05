class Solution {
    public int solution(int n) {
        // java.lang.Math : 수학 계산에 사용할 수 있는 메소드를 제공

        // 제곱수를 구하는 것은 Math 클래스의 pow() 메소드를 이용한다.
        // (ex) Math.pow(5,2) => 5의 2제곱 => 25

        // 해당 수가 제곱수인지 판별하기 위해서는 Math.sqrt(int num) 을 사용한다.
        // 만약 해당 수가 제곱수이면, 제곱근을 구했을 때 소수 자리가 남지 않는다.
        // 따라서 1로 나눈 나머지가 0이어야 한다.
        return Math.sqrt(n) % 1 == 0 ? 1 : 2;
    }
}