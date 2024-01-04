class Solution {
    public String solution(String my_string, int k) {
        StringBuilder sb = new StringBuilder();
        String answer = "";
        
        for(int i = 0; i < k; i++)
            sb.append(my_string);
        
        answer = sb.toString();
        
        return answer;
    }
}