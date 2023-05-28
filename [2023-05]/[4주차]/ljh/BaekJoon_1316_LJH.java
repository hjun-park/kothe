import java.io.*;
public class BaekJoon_1316_LJH {
    /**
     * main 메소드는 나의 풀이
     * 메모리: 14920KB
     * 시간: 140ms
     * */
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine());
        if (n<0 || n>100){
            // Java에서 메인 함수를 강제로 종료시키기 위해서는 System.exit(0)을 사용한다.
            System.exit(0);
        }
        String[] arr = new String[n];
        // 값 저장 및 길이 체크
        for (int i = 0; i<n; i++){
            arr[i] = br.readLine();
            if (arr[i].length()>100){
                System.exit(0);
            }
        }

        // 중복 체크
        for (int i = 0; i<arr.length-1; i++){
            for (int j = arr.length-1; j>i; j--){
                if (arr[i].equals(arr[j])){
                    System.exit(0);
                }
            }
        }

        // 그룹 단어 체크
        for (int i = 0; i<arr.length; i++){
            String[] splitedString = arr[i].split("");
            for (int k = 0; k<splitedString.length-1; k++){
                int isContinuous = 1;
                for (int e = k+1; e<splitedString.length; e++){
                    if (!(splitedString[k].equals(splitedString[e]))){
                        isContinuous = 0;
                    } else{
                        if (isContinuous==0){
                            arr[i] = "false";
                        }
                    }
                }
            }
        }

        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        int result = 0;
        for (int i = 0; i<arr.length; i++){
            if (!(arr[i].equals("false"))){
                result++;
            }
        }
        bw.write(String.valueOf(result));
        bw.flush();
        bw.close();
    }


    /**
     * 뭔가 나의 풀이는 문제의 취지대로 풀지 못 한 것 같다.
     * 따라서 정석적인 풀이 방법을 참고하여, 이렇게 풀 수 있구나 하고 메모하도록 한다.
     * 메모리: 14208KB
     * 시간: 128ms
     */
    public void standardSolution() throws IOException{
        // [전체 로직]
        // - 해당 문제는 한 알파벳 x가 이미 나타났는지 안 나타났는지를 확인해야 한다.
        // - 따라서 boolean형 배열을 선언하는데, 알파벳은 총 26개이므로, 크기가 26인 배열을 선언해준다.
        // -
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(br.readLine()); //몇 개를 입력받을지 정의한다.
        int count = n; // 입력받은 문자열 개수가 일단 다 그룹단어라 가정하고 로직을 수행한다.
        for (int i = 0; i < n; i++){
            // 1. 이미 나타난 문자가 있는지 확인하기 위해 boolean 배열을 선언한다.
            boolean[] arr = new boolean[26];
            // 2. 문자열 입력
            String str = br.readLine();
            // 3. 입력받은 문자열의 첫 번째 단어 확인하여 저장
            arr[(int)str.charAt(0) - 97] = true;
                // => 97을 뺀 이유는, ASCII 코드에서 소문자 알파벳의 상대적 위치를 나타내기 위해서이다.
                // a는 97, b는 98 ... z는 122인데,
                // str.charAt(0)이 a라면 arr[0]에 a에 대한 값을 저장하는 거고,
                // str.charAt(0)이 b라면 arr[1]에 b에 대한 값을 저장하게 되는 것이다.

            // 4. 입력받은 문자열의 첫 번째 단어(idx 0)는 저장했으므로, 두 번째 단어(idx 1)부터 이전 문자와 같은지 검사한다.
            for (int j = 1; j < str.length(); j++){
                char word = str.charAt(j); // 두 번째 단어 추출
                // 5-1. 이전 문자와 같으면 연속되는 문자기 때문에 continue
                if (word == str.charAt(j-1)){
                    continue;
                }

                // 5-2. 만약 이전 문자와 같지 않고, 이미 나타난 문자면 그룹단어가 아니므로 count(그룹단어 개수)에서 1 뺸다.
                if (arr[(int)word -97]){ //이전문자와 같다면 위 if문에서 continue가 되므로, 별도로 이전문자와 같지 않다는 != 연산은 제외해도 된다.
                    count--;                // 즉, 이미 나타난 문자인지 확인.
                    break;
                }
                // 5-3. 이전 문자와 연속되지도 않고, 나타난 적 없는 문자면 다시 알파벳이 나타났는지 체크하는 boolean 배열에 true로 설정한다.
                arr[(int)word - 97] = true;
            }
        }
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(String.valueOf(count));
        bw.flush();
        bw.close();
    }

    }
