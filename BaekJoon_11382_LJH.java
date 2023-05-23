import java.io.*;
import java.util.StringTokenizer;

public class BaekJoon_11382_LJH {
    public static void main(String[] args) throws IOException, NumberFormatException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // 문제 조건은 A,B,C 값이 1이상 10^12 이하값을 요구한다.
        // int형의 최대값은 약 21억(2,147,483,647)이므로 10^12는 담을 수 없다.
        // 따라서 long 자료형을 사용해야 한다.
        long A = Long.parseLong(st.nextToken());
        long B = Long.parseLong(st.nextToken());
        long C = Long.parseLong(st.nextToken());

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // BufferedWriter의 write 메소드는 정수형을 ASCII 코드값으로 출력하게 된다.
        // 따라서 정수형 -> 문자열로 변환 후 출력해줘야 원하는 숫자가 출력된다.
        bw.write(String.valueOf(A+B+C));
        bw.flush();
        bw.close();
    }
}
