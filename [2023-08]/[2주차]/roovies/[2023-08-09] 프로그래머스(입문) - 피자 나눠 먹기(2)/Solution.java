class Solution {
    public int solution(int n) {
        int count = 1;
        while(true) {
            if ((count*6) % n == 0) return count;
            else count++;
        }
    }
}

// 어떻게 풀었는가?
1. 피자를 6조각으로 나눈다.
2. n명이 모두 같은 수의 피자조각을 먹기 위해 몇 판이 필요한가?
3. 즉, 6의 배수이며, n의 배수인 것