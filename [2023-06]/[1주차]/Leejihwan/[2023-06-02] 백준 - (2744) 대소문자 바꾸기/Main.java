import java.io.*;

public class Main {
    public static void main(String[] args) throws IOException {
        // 1. Character 클래스에 있는 toLowerCase()와 toUpperCase()로 풀기
//        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
//        String str = br.readLine();
//        StringBuilder sb = new StringBuilder();
//        for (int i = 0; i < str.length(); i++){
//            char c = str.charAt(i);
//            if (Character.isLowerCase(c)){  // Character.isLowerCase(c) : c가 소문자인지 확인
//                c = Character.toUpperCase(c);   // Character.isUpperCase(c) : c를 대문자로 변경
//            } else{
//                c = Character.toLowerCase(c);
//            }
//            sb.append(c);
//        }
//        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
//        bw.write(sb.toString());
//        bw.flush();
//        bw.close();

        // 2. ASCII 값으로 풀기
        // 65는 A의 값이고, Z는 90이다.
        // 97은 a의 값이고, z는 122이다.
        // 대문자와 소문자는의 차이값은 '32'이다. 이를 활용하면 된다.
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String str = br.readLine();
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < str.length(); i++){
            if (str.charAt(i) >= 65 && str.charAt(i) <= 90){ // 65(A)와 크거나 같고 90(Z) 보다 작거나 같으면 알파벳 대문자
                // Java에서 str.charAt(i) ± 32 연산은 정수형(int)으로 처리된다.
                // 따라서 (char) 을 통해 자료형을 변환해줘야 한다.
                sb.append((char) (str.charAt(i)+32));
            } else if (str.charAt(i) >= 97 && str.charAt(i) <= 122){ // 97(a)와 크거나 같고 122(z) 보다 작거나 같으면 알파벳 소문자
                // Java에서 str.charAt(i) ± 32 연산은 정수형(int)으로 처리된다.
                // 따라서 (char) 을 통해 자료형을 변환해줘야 한다.
                sb.append((char) (str.charAt(i)-32));
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}