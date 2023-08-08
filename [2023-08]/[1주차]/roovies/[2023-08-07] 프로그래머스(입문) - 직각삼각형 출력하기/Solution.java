import java.io.*;

public class Solution {
    public static void main(String[] args) throws IOException {
        // BufferedReader와 BufferedWriter를 사용하기 위해서
        // 1. import java.io.*; 를 해줘야 한다.
        // 2. throws IOException 을 해줘야 한다.
        // 3. BufferedWriter의 개행처리는 .newLine() 또는 .write("\n");을 사용하면 된다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int n = Integer.parseInt(br.readLine());
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < n; i++) {
            sb.append("*");
            bw.write(sb.toString());
            bw.newLine();
        }
        bw.flush();
        bw.close();
    }
}