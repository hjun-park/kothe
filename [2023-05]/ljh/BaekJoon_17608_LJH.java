import java.io.*;

public class BaekJoon_17608_LJH {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int count = Integer.parseInt(br.readLine());
        int [] height = new int[count];
        for (int i = 0; i<count; i++){
            height[i] = Integer.parseInt(br.readLine());
        }
        int maxHeight = height[height.length-1]; //현재까지 가장 높은 높이값 지정 (해당 값보다 작으면 다 안 보임)
        int result = 1; //최종 결과값 (기본적으로 우측에서 바라보면 1개는 무조건 보이므로 1로 설정)
        for (int j = height.length - 1; j>0; j--){
            if (height[j-1] > height[j] && height[j-1] > maxHeight){
                maxHeight = height[j-1];
                result++;
            }
        }
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }
}
