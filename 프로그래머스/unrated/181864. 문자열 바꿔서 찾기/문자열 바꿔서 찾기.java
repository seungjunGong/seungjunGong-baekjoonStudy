class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        
        myString = myString.replace("A", "C"); 
        myString = myString.replace("B", "A");
        
        pat = pat.replace("B", "C");
        
        answer = myString.contains(pat) ? 1 : 0;
        return answer;
    }
}