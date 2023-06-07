import java.io.*;
import java.util.StringTokenizer;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++){
            arr[i] = Integer.parseInt(br.readLine());
        }

        int minBuger = arr[0];
        int minDrink = 0;
        for (int i = 0; i < 2; i++){
            for (int j = 2; j>i; j--){
                if (arr[i]>arr[j]){
                    minBuger = arr[j];
                } else {
                    if (arr[i] > minBuger){
                        continue;
                    } else{
                        minBuger = arr[i];
                    }
                }
            }
        }

        if (arr[3] > arr[4] || arr[3] == arr[4]){
            minDrink = arr[4];
        } else {
            minDrink = arr[3];
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = minBuger + minDrink - 50;
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}