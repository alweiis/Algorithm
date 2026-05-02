package Programmers.Lv1.지폐_접기;

class Solution {
    public int solution(int[] wallet, int[] bill) {
        int answer = 0;

        int walletLong = Math.max(wallet[0], wallet[1]);
        int walletShort = Math.min(wallet[0], wallet[1]);

        int billLong = Math.max(bill[0], bill[1]);
        int billShort = Math.min(bill[0], bill[1]);

        while (billLong > walletLong || billShort > walletShort) {
            billLong /= 2;
            answer++;

            if (billLong < billShort) {
                int temp = billLong;
                billLong = billShort;
                billShort = temp;
            }
        }

        return answer;
    }
}