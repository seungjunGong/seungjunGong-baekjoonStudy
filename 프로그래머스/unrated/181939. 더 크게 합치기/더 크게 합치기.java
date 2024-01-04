class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        int original = Integer.parseInt(String.valueOf(a) + String.valueOf(b));
        int backwards = Integer.parseInt(String.valueOf(b) + String.valueOf(a));
        
        answer = original < backwards ? backwards : original;
        return answer;
    }
}