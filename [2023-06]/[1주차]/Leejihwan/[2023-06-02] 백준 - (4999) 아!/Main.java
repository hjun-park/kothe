import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        String canTalk = br.readLine();
        String doctorWant = br.readLine();
        if ((canTalk.length()-1) >= (doctorWant.length()-1)){
            bw.write("go");
        } else{
            bw.write("no");
        }
        bw.flush();
        bw.close();
    }
}