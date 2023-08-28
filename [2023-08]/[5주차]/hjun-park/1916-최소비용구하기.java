import java.util.*;

public class _1916_최소비용_구하기 {
	static class Node implements Comparable<Node> {
		int node, distance;

		public Node(int node, int distance) {
			this.node = node;
			this.distance = distance;
		}

		@Override
		public int compareTo(Node other) {
			return Integer.compare(this.distance, other.distance);
		}
	}

	static int N, M;
	static List<int[]>[] graph;
	static int[] distance;
	static final int INF = (int) 1e9;

	public static void main(String[] args) {
		Scanner scanner = new Scanner(System.in);
		N = scanner.nextInt();
		M = scanner.nextInt();
		graph = new ArrayList[N + 1];
		distance = new int[N + 1];
		Arrays.fill(distance, INF);

		for (int i = 1; i <= N; i++) {
			graph[i] = new ArrayList<>();
		}

		for (int i = 0; i < M; i++) {
			int a = scanner.nextInt();
			int b = scanner.nextInt();
			int c = scanner.nextInt();
			graph[a].add(new int[]{b, c});
		}

		int start = scanner.nextInt();
		int end = scanner.nextInt();

		dijkstra(start);

		System.out.println(distance[end]);
	}

	static void dijkstra(int start) {
		PriorityQueue<Node> hq = new PriorityQueue<>();
		distance[start] = 0;
		hq.offer(new Node(start, 0));

		while (!hq.isEmpty()) {
			Node current = hq.poll();
			int now = current.node;
			int dist = current.distance;

			if (dist > distance[now]) {
				continue;
			}

			for (int[] next : graph[now]) {
				int nextNode = next[0];
				int cost = dist + next[1];

				if (cost < distance[nextNode]) {
					distance[nextNode] = cost;
					hq.offer(new Node(nextNode, cost));
				}
			}
		}
	}
}
