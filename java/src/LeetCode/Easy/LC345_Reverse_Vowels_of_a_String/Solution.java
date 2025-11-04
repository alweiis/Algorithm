package LeetCode.Easy.LC345_Reverse_Vowels_of_a_String;

import java.util.Set;

class Solution {
    private static final Set<Character> VOWELS = Set.of('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U');

    private static boolean isVowel(char ch) {
        return VOWELS.contains(ch);
    }

    public String reverseVowels(String s) {
        StringBuilder sb = new StringBuilder(s);
        boolean[] isVisited = new boolean[s.length()];
        int rt = sb.length() - 1;

        for (int lt = 0; lt < sb.length(); lt++) {
            if (isVowel(sb.charAt(lt))) {
                while(rt >= 0) {
                    if (isVowel(sb.charAt(rt))) {
                        if (!isVisited[lt] && !isVisited[rt]) {
                            char temp = sb.charAt(lt);
                            sb.setCharAt(lt, sb.charAt(rt));
                            sb.setCharAt(rt, temp);
                            isVisited[rt--] = true;
                            break;
                        }
                    }
                    isVisited[rt--] = true;
                }
            }
            isVisited[lt] = true;
        }
        return sb.toString();
    }
}