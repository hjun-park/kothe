import java.io.*;
import java.util.*;


public class Main {
	static ArrayList<Integer>[] graph;
	static int[] visited;

	public static void dfs(int v) {
		System.out.print(v + " ");
		visited[v] = 1;

		graph[v].forEach(node -> {
			if (visited[node] == 0) {
				dfs(node);
			}
		});
	}

	public static void bfs(int v) {
		Deque<Integer> q = new ArrayDeque<>();
		q.addLast(v);
		visited[v] = 1;

		while (q.size() != 0) {
			int node = q.pollFirst();
			System.out.print(node + " ");

			graph[node].forEach(n -> {
				if(visited[n] == 0) {
					visited[n] = 1;
					q.addLast(n);
				}
			});
		}
	}

	public static void main(String[] args) throws Exception {

		Deque<Integer> q = new ArrayDeque<>();
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());
		int start = Integer.parseInt(st.nextToken());


		// 1. initialize graph as adjacency list
		graph = new ArrayList[N + 1];
		visited = new int[N + 1];
		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}

		// 2. input array
		for (int i = 0; i < M; i++) {
			st = new StringTokenizer(br.readLine());
			int a = Integer.parseInt(st.nextToken());
			int b = Integer.parseInt(st.nextToken());

			graph[a].add(b);
			graph[b].add(a);
		}

		for (int i = 1; i <= N; i++) {
			Collections.sort(graph[i]);
		}

		dfs(start);
		visited = new int[N + 1];
		System.out.println();
		bfs(start);

	}


}
