package LeetCode.Medium.LC443_String_Compression;

class Solution {
    public int compress(char[] chars) {
        // chars.length >= 1 이 보장된 상황이라 별도 검사 생략
        StringBuilder s = new StringBuilder();
        s.append(chars[0]);
        int count = 1;

        for (int i = 1; i < chars.length; i++) {
            char lastChar = s.charAt(s.length() - 1);

            if (lastChar == chars[i]) {
                count++;
            } else {
                if (count > 1) s.append(count);
                s.append(chars[i]);
                count = 1;
            }
        }

        // <- 잘못된 OR 조건 제거: 마지막 그룹이면 count > 1 일 때만 숫자 추가
        if (count > 1) {
            s.append(count);
        }

        // 이제 생성한 압축 문자열을 원본 chars의 앞부분에 덮어쓴다 (in-place 효과)
        char[] compressed = s.toString().toCharArray();
        System.arraycopy(compressed, 0, chars, 0, compressed.length);

        return compressed.length;
    }
}