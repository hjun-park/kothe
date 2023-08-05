class Solution {
    public int solution(String my_string) {
        String str = my_string.replaceAll("[a-zA-Z]", "0");
        String[] arr = str.split("");
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            result += Integer.parseInt(arr[i]);
        }
        return result;
    }
}

// 내 풀이는 a~z와 A~Z를 모두 0으로 변경한 후 배열을 순환하여 덧셈을 했다.
// 불필요한 배열 순환이 존재하고, 정규표현식도 깔끔하지 않다.
// String str = my_string.replaceAll("[^0-9]", "");
// 위처럼 표현하면, 불필요한 0값을 담고 있는 배열을 순환할 필요가 없어진다.