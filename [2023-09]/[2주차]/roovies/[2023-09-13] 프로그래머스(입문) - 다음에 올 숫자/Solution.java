class Solution {
    public int solution(int[] common) {
        int diffValue = common[1] - common[0];

        if (common[2] == (common[1] + diffValue)) return common[common.length-1] + diffValue;
        else return common[common.length-1] * (common[1] / common[0]);
    }
}