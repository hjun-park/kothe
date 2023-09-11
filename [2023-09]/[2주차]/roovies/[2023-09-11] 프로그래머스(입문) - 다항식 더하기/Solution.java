class Solution {
    public String solution(String polynomial) {
        String[] arr = polynomial.split(" ");
        int xCount = 0;
        int constant = 0;

        for (int i = 0; i < arr.length; i++) {
            if (arr[i].contains("x")) {
                xCount = arr[i].length() > 1 ? xCount + Integer.parseInt(arr[i].replace("x", "")) : xCount + 1;
            }

            if (!arr[i].contains("x") && !arr[i].equals("+")) {
                constant += Integer.parseInt(arr[i]);
            }
        }

        StringBuilder sb = new StringBuilder();

        if (xCount > 1 && constant == 0) {
            sb.append(String.valueOf(xCount));
            sb.append("x");
        } else if (xCount > 1 && constant > 0) {
            sb.append(String.valueOf(xCount));
            sb.append("x");
            sb.append(" + ");
            sb.append(String.valueOf(constant));
        } else if (xCount == 1 && constant == 0) {
            sb.append("x");
        } else if (xCount == 1 && constant > 0) {
            sb.append("x");
            sb.append(" + ");
            sb.append(String.valueOf(constant));
        } else if (xCount == 0 && constant > 0) {
            sb.append(String.valueOf(constant));
        } else if (xCount == 0 && constant == 0) {
            sb.append("0");
        }

        return sb.toString();
    }
}