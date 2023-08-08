import java.util.Arrays;

class Solution {
    public int[] solution(String my_string) {
        my_string = my_string.replaceAll("[^0-9]", "");

        int[] arr = new int[my_string.length()];

        for(int i = 0; i < arr.length; i++) {
            arr[i] = Integer.parseInt(String.valueOf(my_string.charAt(i)));
        }
        Arrays.sort(arr);
        return arr;
    }
}


// 스트림 사용

return Arrays.stream(myString.replaceAll("[A-Z|a-z]", "").split("")).sorted().mapToInt(Integer::parseInt).toArray();
// 1. myString.replaceAll("[^0-9]", "").split("") 을 통해 숫자만 남긴 배열을 만들어 스트림을 생성한다.
// 2. sorted() 를 사용하여 문자열 배열을 사전순으로 정렬한다.
// 3. mapToInt(Integer::parseInt) 를 사용하여 정렬된 문자열 배열을 숫자로 변환한다.
//    위 식을 람다식으로 표현하면, mapToInt(value -> Integer.parseInt(value))가 된다.
// 4. toArray() 를 통해 스트림을 배열로 변환하여 반환한다.