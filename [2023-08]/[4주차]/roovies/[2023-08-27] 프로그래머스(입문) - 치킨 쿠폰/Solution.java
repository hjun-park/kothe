// 다른 사람의 풀이
class Solution {
    public int solution(int chicken) {
        int answer = 0;

        // 마지막 서비스를 줄 수 있는 10마리 치킨이 될 때까지 loop를 돈다.
        while (chicken >= 10) {
            // 서비스 치킨 개수는 (받은 치킨 / 10)이 된다. - 쿠폰 10장당 1마리이기 때문
            int newService = chicken / 10;
            // 남은 쿠폰은 (받은 치킨 % 10)으로 나머지가 된다. - 99마리 주문 시 9개 쿠폰이 남기 때문
            int restCoupon = chicken % 10;
            // 이를 토대로 새롭게 서비스를 계산해야 할 총 치킨의 수를 총 쿠폰의 수로 초기화 한다.
            // (새로 서비스 받은 치킨) + (남은 쿠폰의 수)가 새롭게 총 주문량이 된다.
            chicken = newService + restCoupon;

            answer += newService;
        }

        return answer;
    }
}