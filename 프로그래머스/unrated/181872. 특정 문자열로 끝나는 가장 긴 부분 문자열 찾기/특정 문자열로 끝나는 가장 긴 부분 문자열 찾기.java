class Solution {
    public String solution(String myString, String pat) {
        String answer = "";
        int pat_i = pat.length()-1;
        
        for(int i = myString.length()-1; i > -1; i--){
            if(myString.charAt(i) == pat.charAt(pat_i))
                pat_i--;
            else
                pat_i = pat.length()-1;
            
            if(pat_i == -1){
                answer = myString.substring(0, i + pat.length());
                break;                
            }
        }
                
        return answer;
    }
}