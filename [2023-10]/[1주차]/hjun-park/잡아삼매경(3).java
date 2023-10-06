import java.util.*;
import java.io.*;


public class Main {
    static ArrayList<Integer>[] graph;
    static int[] visited;

    static void dfs(int v) {
        /*
            v를 방문했다면 return
            v 방문처리
            v와 인접한 노드들 탐색
                방문하지 않았다면
                 DFS 메서드 시작
         */
        if (visited[v] == 1) {
            return;
        }

        visited[v] = 1;
        graph[v].forEach(node -> {
            if (visited[node] == 0) {
                dfs(node);
            }
        });
    }

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        // graph = 인접리스트 생성 (N+1만큼)
        graph = new ArrayList[N + 1];
        visited = new int[N + 1];
        for (int i = 1; i < N + 1; i++) {
            graph[i] = new ArrayList<>();
        }

        // graph 양옆 이어서 입력받음
        for (int i = 1; i < M + 1; i++) {
            st = new StringTokenizer(br.readLine());
            int start = Integer.parseInt(st.nextToken());
            int end = Integer.parseInt(st.nextToken());
            graph[start].add(end);
            graph[end].add(start);
        }

        // for i in range(1 -> N+1):
        // 방문하지 않았다면 rst +=1 이후 DFS 수행
        int rst = 0;
        for (int i = 1; i < N + 1; i++) {
            if (visited[i] == 0) {
                rst += 1;
                dfs(i);
            }

        }

        System.out.println(rst);
    }

}
