import java.util.*;

class KoTheTest {

	@Test
	void fill_Arrays_fill_리스트를_특정값으로_가득채운다() {
		// 상황: 다익스트라 최초 거리배열 선언 시 모든 리스트 요소들을 무한 값으로 선언한다.
		int N = 5;
		int M = 6;

		// 2d array
		List<int[]>[] graph = new ArrayList[N + 1];
		for(int i = 0; i < N + 1; i++) {
			graph[i] = new ArrayList<>();
		}

		// 1d array
		long[] distance = new long[N + 1];			// 1d array

		// 배열을 최댓값으로 채우기
		Arrays.fill(distance, Integer.MAX_VALUE);

		Assertions.assertEquals(Integer.MAX_VALUE, distance[1]);
	}


}
