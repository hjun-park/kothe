import java.util.*;

class Solution {
    public long solution(String numbers) {
        List<String> list = Arrays.asList("zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine");

        for (int i = 0; i < list.size(); i++) {
            numbers = numbers.replace(list.get(i), String.valueOf(i));
        }

        return Long.parseLong(numbers);
    }
}