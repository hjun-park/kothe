// 나의 풀이
class Solution {
    public String solution(String bin1, String bin2) {
        // 10진수 -> 2진수 변환 메소드 : Integer.toBinaryString() - 반환형은 String
        // Math.pow(Integer.parseInt(b1[i])*2, b1.length - i - 1) 식을 사용했더니 0^0 = 1이 된다.
        String[] b1 = bin1.split("");
        String[] b2 = bin2.split("");
        int a = 0;
        int b = 0;

        for (int i = b1.length - 1; i >= 0; i--) {
            if (i == b1.length - 1 && b1[i].equals("0")) continue;
            a += Math.pow(Integer.parseInt(b1[i])*2, b1.length - i - 1);
        }
        for (int i = b2.length - 1; i >= 0; i--) {
            if (i == b2.length - 1 && b2[i].equals("0")) continue;
            b += Math.pow(Integer.parseInt(b2[i])*2, b2.length - i - 1);
        }
        return Integer.toBinaryString(a+b);
    }
}

// 다른 사람 풀이
📌Integer.parseInt()를 사용할 때, 2번째 인자로 진법을 선택할 수 있다. (default는 10진수이다.)
가령 Integer.parseInt("1010");을 하게 되면, 10진수 1010으로 변환되지만,
Integer.parseInt("1010", 2); 를 하게 되면, 1010을 2진수로 변환하여 10으로 변환된다.
class Solution {
    public String solution(String bin1, String bin2) {
        return Integer.toString(Integer.parseInt(bin1, 2) + Integer.parseInt(bin2, 2),2);
    }
}