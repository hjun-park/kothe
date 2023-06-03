import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int count = Integer.parseInt(st.nextToken());
        int num = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());
        int num2 = 0;
        while (st.hasMoreTokens()){
            num2 = Integer.parseInt(st.nextToken());
            if (num > num2){
                bw.write(String.valueOf(num2) + " ");
            }
        }
        bw.flush();
        bw.close();
    }
}