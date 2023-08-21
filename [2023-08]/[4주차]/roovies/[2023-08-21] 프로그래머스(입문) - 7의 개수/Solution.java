// 나의 풀이
class Solution {
    public int solution(int[] array) {
        int answer = 0;

        for (int i = 0; i < array.length; i++) {
            for (String a : String.valueOf(array[i]).split("")) {
                if (a.equals("7")) answer++;
            }
        }
        return answer;
    }
}

// 스트림 사용
class Solution {
    public int solution(int[] array) {
        return (int) Arrays.stream( // 2. String[]로 변환된 배열을 스트림으로 열고,
                        Arrays.stream(array).mapToObj(String::valueOf).collect(Collectors.joining()).split("") // 1. int[]를 String[] 배열로 변환해주는 stream
                    ).filter(v -> v.equals("7")).count(); // 3. filter()를 통해 "7"과 일치하는 것만 count함. 이때 long형으로 반환되므로 (int)를 통해 return함
    }
}