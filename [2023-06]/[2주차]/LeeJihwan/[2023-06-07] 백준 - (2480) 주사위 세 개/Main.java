import java.io.*;
import java.nio.file.Paths;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int[] arr = new int[3];
        for (int i = 0; i < 3; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }

        int matchCount = 0;
        int matchNum = 0;
        int maxNum = 0;
        for (int i = 0; i < 2; i++){
            for (int j = 2; j>i; j--){
                if (arr[i] == arr[j]){
                    matchCount++;
                    matchNum = arr[i];
                } else {
                    if (arr[i] > arr[j] && arr[i] > maxNum){
                        maxNum = arr[i];
                    } else if (arr[i] < arr[j] && arr[j] > maxNum){
                        maxNum = arr[j];
                    }
                }
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = 0;
        if (matchCount == 3){
            result = 10000+(matchNum*1000);
            bw.write(String.valueOf(result));
        } else if (matchCount == 1) {
            result = 1000+(matchNum*100);
            bw.write(String.valueOf(result));
        } else {
            result = maxNum*100;
            bw.write(String.valueOf(result));
        }
        bw.flush();
        bw.close();
    }
}