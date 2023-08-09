class Solution {
    public String solution(int age) {
        String[] arr = (String.valueOf(age)).split("");
        // 숫자 0의 아스키코드 값은 48이다.
        // 소문자 a의 아스키코드 값은 97이다.
        StringBuilder sb = new StringBuilder();
        for(String a : arr) {
            sb.append((char) (a.charAt(0) + 49));
        }

        return sb.toString();
    }
}

// 스트림 사용
return Arrays.stream(arr).map(v -> String.valueOf((char)(v.charAt(0) + 49))).collect(Collectors.joining());
// map 구문에서 다음과 같이 작성할 시 오류가 발생한다.
// map(v -> (char)(v.charAt(0) + 49))
// 이유는Collectors.joining() 메소드 반환 타입과 map 연산 결과 타입이 일치하지 않기 때문이다.
// Collectors.joining() 반환 타입은 당연히 String인데,
// map(v -> (char)(v.charAt(0) + 49)) 연산 결과 타입은 Character이다.
// 따라서 String.valueOf() 를 통해 String으로 변환해줘야 한다.