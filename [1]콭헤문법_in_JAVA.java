import static org.assertj.core.api.Assertions.*;

import org.junit.jupiter.api.Test;

import java.util.*;
import java.io.*;

public class javaTest {

	@Test
	void Character_관련_메서드() {
		String str = "abcde";
		Character.isLetter(str.charAt(1)); // char 값이 문자이면 true 아니면 false로 리턴
		Character.isDigit(str.charAt(1)); // char 값이 숫자이면 true 아니면 false
		Character.isLetterOrDigit(str.charAt(1)); // char 값이 문자 혹은 숫자 인지
		Character.isAlphabetic(str.charAt(1)); // char 값이 알파벳이면 true 아니면 false

		// 대소문자 확인
		Character.isLowerCase('a'); // true
		Character.isUpperCase('A'); // true

		// 대소문자 변경
		Character.toUpperCase('a'); // A
		Character.toLowerCase('A'); // a

		// 문자 그대로 숫자를 얻을 때
		char c = '1';
		int n = Character.getNumericValue(c); // 1

	}

	@Test
	void Math_관련_메서드() {
		// 1. 최대 최소
		int _max = Math.max(10, 2);
		int _min = Math.min(10, 2);

		// 2. 절대값
		int _abs = Math.abs(-10);

		// 3. 올림 내림 반올림
		double ceil = Math.ceil(-3.2);// -3
		double floor = Math.floor(-3.2);// -4
		long round = Math.round(-3.26);// -3   첫째 자리에서 반올림

		// 3-1. 소수 둘째, 셋째 자리에서 반올림 하고 싶다면
		double doubleNum = 1.23456;
		String stringRound = String.format("%.1f", doubleNum);    // .1f는 둘째자리에서 반올림

		// 4. 제곱
		double doublePow = Math.pow(2, 3);        // 2^3 = 8 => double형
		int intPow = (int) Math.pow(2, 3);

		// 4-1. 제곱근
		double sqrt = Math.sqrt(4);// 2
	}

	@Test
	void String_관련_메서드() {
		String str = "apple";

		// 1. 길이
		int length = str.length();

		// 2. 빈 문자열
		boolean empty = str.isEmpty();

		// 3. 인덱스로 문자 찾기
		char character = str.charAt(0); // 'a'

		// 4. 문자에 해당하는 첫 인덱스 반환
		int idx = str.indexOf("p");     // 1

		// 5. 문자에 해당하는 마지막 인덱스 반환
		int lastIdx = str.lastIndexOf("p");// 2 -> 마지막으로 문자가 속한 인덱스 반환

		// 6. 첫 번째부터 세 번째까지 문자열 반환
		String substring = str.substring(1, 3);// "pp" -> 인덱스 1 이상 3 미만 위치의 문자열 반환

		// 7. [문자치환] p를 e로 모두 변경
		String replacedString = str.replace('p', 'e');  // aeele

		// 8. [정규식 문자 모두 치환] 정규식을 이용하여 모든 문자를 '/' 변경
		String replacedAllString = str.replaceAll(".", "/");  // "/////" -> 정규식에 맞춰 문자 치환 (정규식 "." 은 모든 문자를 의미)

		// 9. 첫 번째 p를 e로 치환
		String replaceFirst = str.replaceFirst("p", "e");     // "aeple"

		// 10. 사전순 문자비교
		/**
		 * str과 applf가 같으면 0
		 * str이 applf보다 사전순으로 앞이면 -1
		 * str이 applf보다 사전순으로 뒤면 1
		 * str과 applf가 마지막 문자만 다르면, 마지막 문자의 사전순 차이 반환
		 */
		int compareTo = str.compareTo("applp");// -1 -> 위 내용 참고

		// 11. 문자 포함 여부 판단
		boolean contains = str.contains("app");

		// 12. 문자열 분리
		String[] split = str.split(" ");    //공백으로 구분된 문자열 str을 분리하여 String[] 배열로 반환

		// 13. 문자 앞뒤 공백 제거
		String trimStr = str.trim();            // str의 앞뒤 공백을 제거한다. 문자열 사이의 공백은 제거하지 않는다.

		// 14. 'a'라는 문자로 시작하는지 판단
		boolean startsWith = str.startsWith("a");// 특정 문자로 시작하는지 판단

		// 15. 'e'라는 문자로 끝나는지 판단
		str.endsWith("e"); // 특정 문자로 끝나는지 판단

		// 16. 모든 문자 대/소문자 변환
		String upperCase = str.toUpperCase();// 모든문자 대문자 변환
		String lowerCase = str.toLowerCase();// 모든문자 소문자 변환
	}

	@Test
	void StringBuilder_관련_메서드() {
		StringBuilder sb = new StringBuilder();

		// 1. sb에 apple 문자열 추가
		sb.append("apple");    // "apple"

		// 2. 2번째 인덱스부터 "oo" 추가
		sb.insert(2, "oo");    // "apoople"

		// 3. 0이상 2미만 삭제
		sb.delete(0, 2);       // "oople"

		// 4. 2번째 인덱스 삭제
		sb.deleteCharAt(2);    // "oole"

		// 5. 1번째 인덱스의 문자를 'p'로 변경
		sb.setCharAt(1, 'p');  // "ople"

		// 6. 문자열 뒤집기
		sb.reverse();          // "elpo"

		// 7. 문자열 절대길이 줄이기
		sb.setLength(2);       // "el"

		// 8. 문자열 절대길이 늘이기
		sb.setLength(4);       // "el  " -> 뒤가 공백으로 채워짐
	}

	@Test
	void List_관련_메서드() {
		List<String> list = new ArrayList<>();
		List<String> list2 = new ArrayList<>();

		// 1. "one" 요소 삽입
		list.add("one");

		// 2. 0번째 인덱스에 "zero" 요소 삽입
		list.add(0, "zero");

		// 3. list2의 모든 요소를 list에 삽입
		list.addAll(list2);

		// 4. "zero" 문자의 인덱스 반환
		list.indexOf("zero");    // 0

		// 5. "zero" 문자의 마지막 인덱스 반환
		list.lastIndexOf("zero");

		// 6. 0번째 인덱스 값 삭제
		list.remove(0);

		// 7. 특정 값을 이용하여 요소 삭제
		list.remove("one");

		// 8. list에서 list2에 있는 요소 모두 삭제 (차집합)
		list.removeAll(list2);

		// 9. list에서 list2에 있는 요소를 제외하고 모두 삭제 (교집합)
		list.retainAll(list2);

		// 10. 리스트 특정요소 "one" 있는지 체크
		list.contains("one");

		// 11. list에 list2의 모든 값이 다 들어 있는지 확인
		list.containsAll(list2);

		// 12. 람다식 이용하여 짝수인 요소를 모두 제거
		List<Integer> numList = List.of(1, 2, 3, 4, 5);
		numList.removeIf(x -> x % 2 == 0);
	}


	@Test
	void arrays_관련_메서드() throws Exception {
		int[] arr = {10, 8, 11, 2, 3, 0};

		// 1. int[] 배열 arr를 List로 변환
		List<Integer> list = Arrays.stream(arr).boxed().toList();

		// 2. int[] -> Integer[]
		Integer[] integerList = Arrays.stream(arr).boxed().toArray(Integer[]::new);

		// 3. int[] 배열 0번 ~ 3번 인덱스까지 복사
		int[] copyOfRange = Arrays.copyOfRange(arr, 0, 3);
		System.out.println("copyOfRange = " + Arrays.toString(copyOfRange));

		// 4. 오름차순 {0, 2, 3, 8, 10, 11}
		Arrays.sort(arr);
		System.out.println("arr = " + Arrays.toString(arr));

		// 5. 내림차순 {11, 10, 8, 3, 2, 0}
		Collections.reverse(Arrays.asList(arr));
		System.out.println("arr = " + Arrays.toString(arr));

		// 6. 일부만 정렬 ((0~4만 정렬))) {2, 8, 11, 10, 3, 0}
		Arrays.sort(arr, 0, 4);

		// 7. 오름차순 정렬 후 binary Search 진행하여 '2' 라는 값 찾기
		Arrays.sort(arr);
		int binResult = Arrays.binarySearch(arr, 2);


		int[][] items = new int[][]{{1, 2}, {3, 4}, {5, 6}};

		// 8. 람다를 이용하여 2차원 배열 행 정렬
		Arrays.sort(items, (o1, o2) -> {
			// 행 먼저
			if (o1[1] == o2[1]) return o1[0] - o2[0];

				// 다음 열 정렬
			else return o1[1] - o2[1];
		});

		// deepToString 으로 모두 출력
		System.out.println("items = " + Arrays.deepToString(items));

		// 9. 일반배열 리스트 생성 후 복제
		int[] tmp = arr.clone();

		// 10. 배열에서 최대값 구하기 (stream)
		int max = Arrays.stream(arr).max().getAsInt();

		// 11. 배열에서 최소값 구하기 (stream)
		int min = Arrays.stream(arr).min().getAsInt();

		// 12. 배열에서 총계 구하기 (stream)
		int sum = Arrays.stream(arr).sum();
	}


	@Test
	void list_to_array() {

		String[] temp1 = {"apple", "banana", "lemon"};
		// 1. String[] -> List<String>
		List<String> stringArrayToList = new ArrayList<>(Arrays.asList(temp1));


		List<String> list = new ArrayList<>();
		// 2. List<String> -> String[]
		String[] rst1 = list.toArray(new String[list.size()]);


		int[] temp = {1, 2, 3, 4};
		// 3. int[] -> List<Integer>
		List<Integer> rst2 = Arrays.stream(temp).boxed().toList();


		List<Integer> arrayList = new ArrayList<>();
		// 4. List<Integer> -> int[]
		int[] rst3 = arrayList.stream().mapToInt(x -> x).toArray();
	}

	@Test
	void Collections_관련_메서드() {
		int[] temp = {1, 2, 3, 10, 20};
		List<Integer> list = new ArrayList<>(List.of(temp));

		// 1. List에서 max, min 구하기
		Integer max = Collections.max(list);
		Integer min = Collections.min(list);

		// 2. 오름차순으로 정렬
		List<String> list2 = List.of("A, B, C, a");
		Collections.sort(list2);
		System.out.println("오름차순 : " + list2);

		// 3. 내림차순으로 정렬
		Collections.sort(list2, Collections.reverseOrder());
		System.out.println("내림차순 : " + list2);


		// 4. 대소문자 구분없이 오름차순
		Collections.sort(list2, String.CASE_INSENSITIVE_ORDER);
		System.out.println("대소문자 구분없이 오름차순 : " + list2); // [a, A, B, C]


		// 5. 대소문자 구분없이 내림차순
		Collections.sort(list2, Collections.reverseOrder(String.CASE_INSENSITIVE_ORDER));
		System.out.println("대소문자 구분없이 내림차순 : " + list2); // [C, B, a, A]

		// 6. List 뒤집기
		Collections.reverse(list2);

		// 7. List 내 원소의 갯수 반환 (python의 counter)
		int frequency = Collections.frequency(list2, "A");

		//List 내 원소를 이진탐색을 이용해 찾기
		//반드시 정렬 후 수행
		Collections.sort(list2);
		int idx = Collections.binarySearch(list2, "C");
		System.out.println("list = " + list2);
		System.out.println("idx = " + idx);
	}

	@Test
	void queue_관련_메서드() {
		Queue<Integer> queue = new LinkedList<>();

		// 1. 값 추가
		queue.add(1);

		// 2. 첫 번째 값 꺼내고 반환, 비어있으면 null 반환
		Integer poll = queue.poll();

		// 3. 첫 번째 값 제거
		Integer remove = queue.remove();

		// 4. 값 모두 삭제
		queue.clear();

		// 5. 첫 번째 값 출력 (제거 X)
		Integer peek = queue.peek();

		// 6. 1을 포함하고 있으면 true, 아니면 false
		boolean contains = queue.contains(1);
	}

	@Test
	void deque_관련_메서드() {
		Deque<Integer> deque = new ArrayDeque<>();
		deque.addFirst(1); // 1
		deque.addLast(2); // 1 2
		boolean contains = deque.contains(1);// true
		Integer first = deque.getFirst();// 1
		Integer last = deque.getLast();// 2
		Integer peekFirst = deque.peekFirst();	// 1
		// 이외 poll 및 remove도 있음
	}

	@Test
	void hashSet_메서드() {
      /*
         HashSet : 중복 허용 X, 순서 X
         LinkedHashSet : 중복 허용 X, 순서 O (삽입순)
         TreeSet : 중복 허용 X, 이진탐색트리 형태로 데이터 저장, 정렬 O
       */
		HashSet<Integer> hashSet = new HashSet<>();
		HashSet<Integer> hashSet2 = new HashSet<>();

		// 1. 요소 추가
		hashSet.add(1);

		// 2. 요소 삭제
		hashSet.remove(1);    // 값이 1인 요소 삭제

		// 3. 차집합
		hashSet.removeAll(hashSet2);    //hashSet의 데이터 중 hashSet2과 중복된 데이터를 모두 삭제

		// 4. 교집합
		hashSet.retainAll(hashSet2);    //hashSet의 데이터 중 hashSet2과 중복된 데이터만 남기고 나머지 모두 삭제

		// 5. 데이터 초기화
		hashSet.clear();

		// 6. hashSet 사이즈 확인
		int size = hashSet.size();

		// 7. 특정 요소 포함 여부 확인
		boolean contains = hashSet.contains(1);

		// 방법 2: for-each문으로 원소에 접근
		for (int item : hashSet)
			System.out.println(item);

	}

	@Test
	void treeSet_관련_메서드() {
		// 선언
		TreeSet<Integer> ts = new TreeSet<>(); // 오름차순 정렬
		TreeSet<Integer> ts2 = new TreeSet<>(Collections.reverseOrder()); // 내림차순 정렬

		// 추가
		ts.add(5);
		ts.add(2);
		ts.add(1);
		ts.add(3); // [1,2,3,5]

		// 값 반환
		ts.first(); // 첫 데이터 반환 1
		ts.last(); // 마지막 데이터 반환 5

		// 삭제
		ts.remove(5); // 5 삭제 [1,2,3]
		ts.pollFirst(); // 첫 데이터 삭제 [2,3]
		ts.pollLast(); // 마지막 데이터 삭제 [2]
		ts.clear(); // 전체 삭제 []

		// 크기
		ts.size();
	}

	@Test
	void hashMap_메서드() {
      /*
         HashMap : key - value 형태로 데이터 저장, 순서 XHashMap : <key, value>쌍, value의 중복 허용 O, 순서 X
         LinkedHashMap : <key, value>쌍, value의 중복 허용 O, key 순서 O (삽입순)
         TreeMap : <key, value>쌍, key 순서가 오름차순(알파벳순) 으로 정렬됨
       */
		HashMap<Integer, String> hashMap = new HashMap<>();

		//요소 추가
		hashMap.put(1, "딸기");
		hashMap.put(2, "바나나");
		hashMap.put(1, "사과");    // (1. "딸기")의 value가 "사과"로 대체됨

		//요소 삭제
		hashMap.remove(1);    // key 가 1인 요소 삭제

		//전체 삭제
		hashMap.clear();

		//key 포함 여부 확인
		boolean b = hashMap.containsKey(1);

		//value 포함 여부 확인
		boolean value = hashMap.containsValue("사과");

		//key - value 출력
		for (Integer key : hashMap.keySet()) {
			System.out.println(key + " " + hashMap.get(key));
		}

		// stream
		hashMap.entrySet().stream().forEach(System.out::println);

	}

	@Test
	void stream_활용_hashmap_key_가져오기() {

		Map<String, Integer> hashMap = new HashMap();
		hashMap.put("A", 1);
		hashMap.put("B", 2);
		hashMap.put("C", 3);

		System.out.println(getKey(hashMap, 2));        // 인쇄물 `B`
	}

	@Test
	void 깊은복사() {
		ArrayList<Integer> arrList_A = new ArrayList<Integer>();
		ArrayList<Integer> arrList_B = new ArrayList<Integer>();
		arrList_A.addAll(arrList_B);
	}

	@Test
	void setToList() {
		Set<String> set = new HashSet<String>();
		List<String> menuList = new ArrayList<>(set);
	}

	@Test
	void int배열_자르기() {
		int[] array = {1, 2, 3, 4, 5};
		int[] temp = Arrays.copyOfRange(array, 1, 3);
		System.out.println(temp);
	}

	@Test
	void 리스트배열_자르기() {
		ArrayList<Integer> testData = new ArrayList();
		for (int data = 0; data < 10; data++) {
			testData.add(data);
		}
		System.out.println(testData);
		System.out.println(testData.subList(1, testData.size() - 1));

		//출력 결과
		//      [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
		//      [1, 2, 3, 4, 5, 6, 7, 8]
	}

	@Test
	void 이차원배열_출력() {
		int[][] arr = {{1, 2, 3, 4, 5}, {5, 4, 3, 2, 1}};
		System.out.println(Arrays.deepToString(arr));
	}

	@Test
	void 배열요소_모두_더하기() {
		int arr[] = new int[]{12, 34, 45, 21, 33, 4};
		int sum = Arrays.stream(arr).sum();
		System.out.println("Array Sum = " + sum);
	}

	@Test
	void 일반배열_중복제거() {
		int[] A = {1, 2, 3, 4, 1, 1};
		Arrays.stream(A).distinct().toArray();
	}

	@Test
	void 배열_중복제거() {
		List<Integer> intList = List.of(1, 2, 3, 4, 1, 1);
		List result = intList.stream().distinct().collect(Collectors.toList());
	}

	@Test
	void bufferedReader_사용() {
      /*
         BurredReader 클래스는 Enter를 경계로 입력값을 인식한다.
         readLine() 메소드는 개행문자(Enter)를 포함해 String 형식으로 입력을 받아온다.
         따라서, int형으로 readLine() 을 받아오려면 Integer.pareseInt() 로 형변환이 필요하다.
       */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int N = Integer.parseInt(br.readLine());
		System.out.prin(N);
	}

	@Test
	void StringTokenizer_사용() {
      /*
         StringTokenizer 클래스는 지정한 형식에 따라 문자열을 쪼개주는 클래스이다.
         new StringTokenizer(문자열,기준) 형식으로 StringTokenizer 객체를 생성할 수 있다.
       */
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		System.out.print(N + " " + M);
	}

	@Test
	void 이차원_배열_string_tokenizer() {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringTokenizer st = new StringTokenizer(br.readLine());

		int N = Integer.parseInt(st.nextToken());
		int M = Integer.parseInt(st.nextToken());

		int[][] arr = new int[N][M];
		for (int i = 0; i < N; i++) {
			String str = br.readLine();
			for (int j = 0; j < M; j++) {
				arr[i][j] = Integer.parseInt(String.valueOf(str.charAt(j)));
			}
		}
		System.out.print(N + " " + M);
		for (int i = 0; i < N; i++) {
			for (int j = 0; j < M; j++) {
				System.out.print(arr[i][j]);
			}
			System.out.println();
		}
	}

	@Test
	void Queue에서의_pair_연산자_할용() {
		static class Node {
			int y;
			int x;
			int dist;

			Node(int y, int x, int dist) {
				this.y = y;
				this.x = x;
				this.dist = dist;
			}
		}

		Queue<Node> queue = new LinkedList<>();
		queue.add(new Node(1, 2, 3));
		Node node = queue.poll();
	}

	@Test
	void Priority_Queue_에서의_Pair_연산자_활용() {
		static class Node {
			int y;
			int x;

			Node(int y, int x) {
				this.y = y;
				this.x = x;
			}

			public int compareTo(Node p) {
				if (this.y < p.x) {
					return -1; // 오름차순
				} else if (this.y == p.y) {
					if (this.x < p.x) {
						return -1;
					}
				}
				return 1;
			}
		}

		PriorityQueue<Node> pq1 = new PriorityQueue<>(Node::compareTo);
		pq1.add(new Node(1, 2));
		pq1.add(new Node(1, 1));
		pq1.add(new Node(2, 3));
		pq1.add(new Node(2, 1));

		while (!pq1.isEmpty()) {
			Node node = pq1.peek();
			System.out.println(node.y + " " + node.x);
			pq1.remove();
		}
	}

	@Test
	void 우선순위큐() {
      /*
         오름차순
      */
		PriorityQueue<Integer> ipq = PriorityQueue < Integer > ();
		PriorityQueue<String> spq = PriorityQueue < String > ();

      /*
         내림차순 (min hq)
      */
		PriorityQueue<Integer> pq = PriorityQueue < Integer > (Collections.reverseOrder());

		// heapq에서 값을 꺼냄
		pq.peek();

		PriorityQueue<Integer> pq = new PriorityQueue<>();
		// 기본은 낮은 숫자가 우선순위를 갖는다.
		// 높은 숫자가 우선되게 하려면 () 안에 Collections.reverseOrder() 작성

		pq.add(1); // 값 추가
		pq.offer(1); // 값 추가
		pq.poll(); // 첫 번째 값 반환, 비어있으면 null 반환
		pq.remove(); // 첫 번째 값 제거
		pq.clear(); // 값 모두 삭제
		pq.peek(); // 첫 번째 값 출력 (제거 X)
	}

	@Test
	void adjacentList_인접리스트() {
		// 단 방향 [출발노드,도착노드] 가 주어졌을 때
		int[][] arr =[[1, 3],[1, 5],[3, 2],[3, 4],[5, 4],[5, 6],[2, 4],[4, 6]];

		ArrayList<ArrayList<Integer>> list = new ArrayList<>();

		// 인접리스트 초기화
		for (int i = 0; i <= arr.length; i++) {
			list.add(new ArrayList<>());
		}

		// 양방향 인접리스트
		for (int i = 0; i < arr.length; i++) {
			int start = arr[i][0], end = arr[i][1];
			list.get(start).add(end);
			list.get(end).add(start);
		}
	}

	@Test
	void 삼차원_리스트() {
		int N = 5;

		static ArrayList<Integer>[][] map;
		map = new ArrayList[N + 1][N + 1];
		for (int i = 1; i <= N; i++) {
			for (int j = 1; j <= N; j++) {
				map[i][j] = new ArrayList<Integer>();
			}
		}
	}

	static <K, V> K getKey(Map<K, V> map, V value) {
		return map.entrySet().stream()
			.filter(entry -> value.equals(entry.getValue()))
			.findFirst().map(Map.Entry::getKey)
			.orElse(null);
	}

}
