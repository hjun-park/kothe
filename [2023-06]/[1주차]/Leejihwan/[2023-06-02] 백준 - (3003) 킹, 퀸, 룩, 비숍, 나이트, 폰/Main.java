import java.io.*;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        int king = Integer.parseInt(st.nextToken());
        int queen = Integer.parseInt(st.nextToken());
        int rook = Integer.parseInt(st.nextToken());
        int bishop = Integer.parseInt(st.nextToken());
        int knight = Integer.parseInt(st.nextToken());
        int pawn = Integer.parseInt(st.nextToken());

        king = 1 - king;
        queen = 1 - queen;
        rook = 2 - rook;
        bishop = 2 - bishop;
        knight = 2 - knight;
        pawn = 8 - pawn;

        StringBuilder sb = new StringBuilder();
        sb.append(king + " ");
        sb.append(queen + " ");
        sb.append(rook + " ");
        sb.append(bishop + " ");
        sb.append(knight + " ");
        sb.append(pawn + " ");

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(sb.toString());
        bw.flush();
        bw.close();
    }
}