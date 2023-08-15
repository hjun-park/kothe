class Solution {
    public String solution(String letter) {
        String[] mos = {".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."};

        String[] letterArr = letter.split(" ");
        StringBuilder sb = new StringBuilder();
        char c = 0;

        for (int i = 0; i < letterArr.length; i++) {
            for (int j = 0; j < mos.length; j++) {
                c = (char) (j+97);
                if (letterArr[i].equals(mos[j])) sb.append(c);
            }
        }
        return sb.toString();
    }
}