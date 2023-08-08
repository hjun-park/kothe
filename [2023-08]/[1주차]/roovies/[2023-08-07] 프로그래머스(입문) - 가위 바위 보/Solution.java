class Solution {
    public String solution(String rsp) {
        String[] arr = rsp.split("");
        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < arr.length; i++) {
            if(arr[i].equals("2")) sb.append("0");
            if(arr[i].equals("0")) sb.append("5");
            if(arr[i].equals("5")) sb.append("2");
        }
        return sb.toString();
    }
}

// 스트림으로 표현하면 다음과 같이 표현할 수 있다.
return Arrays.stream(rsp.split("")).map(s -> s.equals("2") ? "0" : s.equals("0") ? "5" : "2").collect(Collectors.joining());

// 1. rsp.split("")을 통해 배열 스트림을 생성한다.
// 2. 각각의 스트림 요소(각 배열의 원소)에 3항 연산자를 통해 조건에 따라 다른 값으로 반환한다.
// 3. map으로 반환된 배열을 collect(Collectors.joining())을 통해 문자열로 변환한다.
//    Collectors.joining() : 빈 문자열을 사용하여 요소들을 연결하여 하나의 문자열로 만들어줌