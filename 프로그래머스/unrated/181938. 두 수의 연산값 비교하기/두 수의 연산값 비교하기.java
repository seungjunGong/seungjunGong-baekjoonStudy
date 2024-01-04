class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int original = Integer.parseInt("" + a + b);
        int multiple = 2 * a * b;
        
        answer = original >= multiple ? original : multiple;
        return answer;
    }
}