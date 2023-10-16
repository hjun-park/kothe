import java.io.*;
import java.util.*;

public class Solution {
    public static int solution(int n) {
        int answer = 0;
        if (n % 2 == 0) {
            while(0 < n) {
                answer += n * n;
                n -= 2;
            }
        }

        if (n % 2 != 0) {
            while(0 < n) {
                answer += n;
                n -= 2;
            }
        }
        return answer;
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        System.out.println(solution(Integer.parseInt(br.readLine())));
    }
}