import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int [] arr = new int[30];
        int input = 0;
        for (int i = 0; i < 28; i++){
            input = Integer.parseInt(br.readLine());
            arr[input-1] = 1;
        }
        for (int i = 0; i < 30; i++){
            if (arr[i] != 1){
                bw.write(String.valueOf(i+1));
                bw.newLine();
            }
        }
        bw.flush();
        bw.close();
    }
}