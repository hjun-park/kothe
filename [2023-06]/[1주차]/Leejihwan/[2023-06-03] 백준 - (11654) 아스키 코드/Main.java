import java.io.*;


public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // char형을 int형으로 저장하면 그 문자는 아스키 코드로 변환된다!!
        int ascii = br.readLine().charAt(0);
        // 이때 String.valueOf()를 사용하지 않으면, 해당 값을 자동으로 변환해서 출력하기 때문에
        // 숫자값 자체로 출력될 수 있도록, 숫자 자체를 문자열로 변환해준다.
        bw.write(String.valueOf(ascii));
        bw.flush();
        bw.close();
    }
}