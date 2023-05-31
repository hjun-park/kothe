import java.io.*;
import java.math.BigInteger;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        // BigInteger 입력받기
        BigInteger n = new BigInteger(st.nextToken());
        BigInteger m = new BigInteger(st.nextToken());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        // BigInteger의 나누기는 devide() 를 사용한다.
        BigInteger money = n.divide(m);
        // BigIntger의 나머지는 remainder() 를 사용한다.
        BigInteger left = n.remainder(m);
        bw.write(String.valueOf(money) + "\n" + String.valueOf(left));
        bw.flush();
        bw.close();
    }
}