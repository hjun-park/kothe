import java.io.*;
import java.math.BigInteger;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BigInteger a = new BigInteger(br.readLine());
        BigInteger b = new BigInteger(br.readLine());
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(a.add(b)));
        bw.newLine();
        // BigInteger에서 빼기는 subtract()를 사용한다.
        bw.write(String.valueOf(a.subtract(b)));
        bw.newLine();
        bw.write(String.valueOf(a.multiply(b)));
        bw.newLine();
        bw.flush();
        bw.close();
    }
}