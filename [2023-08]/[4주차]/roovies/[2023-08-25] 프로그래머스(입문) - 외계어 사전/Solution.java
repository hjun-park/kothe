import java.util.Arrays;
import java.util.stream.Collectors;

class Solution {
    public int solution(String[] spell, String[] dic) {
        int count = 0;
        for (int i = 0; i < dic.length; i++) {
            for (int j = 0; j < spell.length; j++) {
                if(dic[i].contains(spell[j])) count++;
            }
            if (count == spell.length) return 1;
            else count = 0;
        }
        return 2;
    }
}