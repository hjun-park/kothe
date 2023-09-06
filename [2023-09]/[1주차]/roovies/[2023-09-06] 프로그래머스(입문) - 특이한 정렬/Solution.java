import java.util.Arrays;

class Solution {
    public int[] solution(int[] numlist, int n) {
        for (int i = 0; i < numlist.length; i++) {
            numlist[i] -= n;
        }

        int tmp = 0;
        for (int i = 0; i < numlist.length; i++) {
            for (int j = numlist.length - 1; j > i; j--) {
                if (Math.abs(numlist[i]) > Math.abs(numlist[j])) {
                    tmp = numlist[i];
                    numlist[i] = numlist[j];
                    numlist[j] = tmp;
                } else if (Math.abs(numlist[i]) == Math.abs(numlist[j])) {
                    if (numlist[i] < numlist[j]) {
                        tmp = numlist[i];
                        numlist[i] = numlist[j];
                        numlist[j] = tmp;
                    }
                }
            }
        }

        for (int i = 0; i < numlist.length; i++) {
            numlist[i] += n;
        }

        return numlist;
    }
}