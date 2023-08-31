import java.io.*;
import java.util.*;

class Edge {
	int start, end, time;
	public Edge(int start, int end, int time) {
		this.start = start;
		this.end = end;
		this.time = time;
	}
}

public class _11657_타임머신 {
	private static BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
	private static BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));

	static int v, e;
	static long distance[];
	static Edge edges[];

	public static void main(String[] args) throws IOException {
		StringTokenizer st = new StringTokenizer(br.readLine());

		v = Integer.parseInt(st.nextToken());
		e = Integer.parseInt(st.nextToken());
		edges = new Edge[e + 1];
		distance = new long[v + 1];
		Arrays.fill(distance, Integer.MAX_VALUE);

		for (int i = 0; i < e; i++) {
			st = new StringTokenizer(br.readLine());
			int start = Integer.parseInt(st.nextToken());
			int end = Integer.parseInt(st.nextToken());
			int time = Integer.parseInt(st.nextToken());
			edges[i] = new Edge(start, end, time);
		}

		// 벨만-포드 알고리즘
		distance[1] = 0;
		for(int i = 1; i < v; i++) {
			for(int j = 0; j < e; j++) {
				Edge edge = edges[j];

				// 최단거리 여부 체크
				if(distance[edge.start] != Integer.MAX_VALUE
					&& distance[edge.end] > distance[edge.start] + edge.time) {
					distance[edge.end] = distance[edge.start] + edge.time;
				}
			}
		}

		boolean isCycle = false;

		for(int i = 0; i < e; i++) {
			Edge edge = edges[i];

			if(distance[edge.start] != Integer.MAX_VALUE
				&& distance[edge.end] > distance[edge.start] + edge.time) {
				isCycle = true;
				break;
			}
		}

		if(!isCycle) {
			for(int i = 2; i < v+1; i++) {
				if(distance[i] == Integer.MAX_VALUE) {
					System.out.println("-1");
				}
				else {
					System.out.println(distance[i]);
				}
			}
		} else {
			System.out.println("-1");
		}
	}
}
