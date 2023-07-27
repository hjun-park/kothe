class Solution {
    public int[] solution(String[] strlist) {
        int[] arr = new int[strlist.length];
        int j = 0;
        for (String a : strlist) {
            arr[j] = a.length();
            j++;
        }
        return arr;
    }
}