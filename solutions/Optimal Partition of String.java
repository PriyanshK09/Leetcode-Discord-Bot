class Solution {
    public int partitionString(String s) {
        int count = 0;
        int idx = 0;
        while (idx < s.length()) {
            Set<Character> set = new HashSet<>();
            while (idx < s.length() && set.add(s.charAt(idx))) {
                idx++;
            }
            count++;
        }
        return count;
    }
}
