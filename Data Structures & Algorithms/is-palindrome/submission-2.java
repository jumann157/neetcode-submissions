class Solution {
    public boolean isPalindrome(String s) {
        int left = 0;
        int right = s.length() - 1;

        // .,
        // lr
        // l = 2, r = 1 s.length = 2


        while(right > left) {
            // check left
            while(left < s.length() && !Character.isLetterOrDigit(s.charAt(left))) {
                System.out.println(s.charAt(left) + " : " + left);
                left++;
            }

            // check right
            while(right >= 0 && !Character.isLetterOrDigit(s.charAt(right))) {
                System.out.println(s.charAt(right) + " : " + right);
                right--;
            }

            if(left >= s.length() || right < 0) {
                break;
            }

            // check if NOT equal
            if(Character.toLowerCase(s.charAt(left)) != Character.toLowerCase(s.charAt(right))) {
                System.out.println(s.charAt(left) + " != " + s.charAt(right) + " = false");
                return false;
            }
            left++;
            right--;
        }

        return true;
    }
}
