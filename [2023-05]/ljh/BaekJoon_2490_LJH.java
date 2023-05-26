import java.io.*;
import java.util.StringTokenizer;

public class BaekJoon_2490_LJH {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int [] arr = new int[3];
        int temp = 0;
        for (int i = 0; i<3; i++){
            arr[i] = Integer.parseInt(st.nextToken());
        }
        for (int i = 0; i<3; i++){
            for (int j = 2; j>i; j--){
                if (arr[i] > arr[j]){
                    temp = arr[i];
                    arr[i] = arr[j];
                    arr[j] = temp;
                }
            }
        }
        for (int i = 0; i<3; i++){
            bw.write(String.valueOf(arr[i]) + " ");
        }
        bw.flush();
        bw.close();
    }
}
