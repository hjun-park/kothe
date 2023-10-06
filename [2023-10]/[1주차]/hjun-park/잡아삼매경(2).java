[좋다]

import java.util.*;
import java.io.*;

/*
10
1 2 3 4 5 6 7 8 9 10
 */
public class Main {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        st = new StringTokenizer(br.readLine());

        long[] A = new long[N];

        for (int i = 0; i < N; i++) {
            A[i] = Integer.parseInt(st.nextToken());
        }
        Arrays.sort(A);

        int rst = 0;
        for (int i = 0; i < N; i++) {
            long target = A[i];
            int l = 0;
            int r = N-1;

            while(l < r) {
                long _sum = A[l] + A[r];

                if(_sum == target) {
                    if(l != i && r != i) {
                        rst += 1;
                        break;
                    } else if (l == i) {
                        l += 1;
                    } else if (r == i) {
                        r -= 1;
                    }
                } else if (_sum < target) {
                    l += 1;
                } else {
                    r -= 1;
                }

            }
        }

        System.out.println(rst);
    }


}
