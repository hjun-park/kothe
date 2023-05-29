import java.io.*;

public class Solution {
    public String solution(String code){
        int mode = 0;
        StringBuilder sb = new StringBuilder();
        for(int i = 0; i < code.length(); i++){
            if(mode == 0){
                if(!(code.charAt(i) == '1')){
                    if(i % 2 == 0){
                        sb.append(code.charAt(i));
                    }
                } else{
                    mode = 1;
                }
            } else{
                if(!(code.charAt(i) == '1')){
                    if(i % 2 != 0){
                        sb.append(code.charAt(i));
                    }
                } else {
                    mode = 0;
                }
            }
        }
        String ret = sb.toString();
        if(ret.equals("")){
            ret = "EMPTY";
        }
        return ret;
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String code = br.readLine();
        Solution s = new Solution();
        String ret = s.solution(code);
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        bw.write(ret);
        bw.flush();
        bw.close();
    }
}