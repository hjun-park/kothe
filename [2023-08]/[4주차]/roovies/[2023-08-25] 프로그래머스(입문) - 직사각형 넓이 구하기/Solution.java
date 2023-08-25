class Solution {
    public int solution(int[][] dots) {
        int width = 0;
        int height = 0;

        for (int i = 1; i < dots.length; i++) {
            for (int j = 0; j < 2; j++) {
                if (dots[0][0] == dots[i][0]){
                    height = Math.abs(dots[0][1] - dots[i][1]);
                } else if(dots[0][1] == dots[i][1]) width = Math.abs(dots[0][0] - dots[i][0]);
            }
        }

        return width * height;

    }
}