class Solution {
    public int[] solution(String[] keyinput, int[] board) {
        int maxWidth = (board[0] - 1) / 2;
        int maxHeight = (board[1] - 1) / 2;
        int currentWidth = 0;
        int currentHeight = 0;

        for (int i = 0; i < keyinput.length; i++) {
            if (keyinput[i].equals("left")) {
                if (currentWidth == (maxWidth * - 1)) continue;
                currentWidth -= 1;
            } else if (keyinput[i].equals("right")) {
                if (currentWidth == maxWidth) continue;
                currentWidth += 1;
            } else if (keyinput[i].equals("down")) {
                if (currentHeight == (maxHeight * - 1)) continue;
                currentHeight -= 1;
            } else if (keyinput[i].equals("up")) {
                if (currentHeight == maxHeight) continue;
                currentHeight += 1;
            }
        }

        int[] answer = {currentWidth, currentHeight};
        return answer;
    }
}