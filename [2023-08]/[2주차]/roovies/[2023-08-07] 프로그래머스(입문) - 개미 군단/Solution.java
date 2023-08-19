class Solution {
    public int solution(int hp) {
        int count = 0;
        if (hp % 5 != 0) {
            if ((hp % 5) % 3 != 0) {
                count = (hp / 5) + (hp % 5) / 3 + (hp % 5) % 3;
            }
            else count = (hp / 5) + (hp % 5) / 3;
        } else {
            count = hp / 5;
        }
        return count;
    }
}

// 위 경우 다음처럼 한 줄로 처리해줄 수 있다.
return hp / 5 + (hp % 5 / 3) + hp % 5 % 3;
// 위 식이 왜 가능하냐면,
// [ hp가 4라면 ]
// 1. hp / 5 가 0.8이기 때문에 int형이므로 0이 된다.
// 2. (hp % 5 / 3)은 연산자 우선순위로 인하여 4 / 3이므로, int형이기 때문에 1이 된다.
// 3. hp % 5 % 3은 4 % 5가 4이고, 4%3이 되므로 1이 된다.
// 따라서 3공격력 개미 1마리, 1공격력 개미 1마리인 총 2마리 개미 개수가 나오게 된다.