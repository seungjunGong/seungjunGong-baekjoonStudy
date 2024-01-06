class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        int i = 0;
        while(myString.indexOf(pat, i) != -1){
            i = myString.indexOf(pat, i) + 1;
            answer += 1;
        }
        
        return answer;
    }
}