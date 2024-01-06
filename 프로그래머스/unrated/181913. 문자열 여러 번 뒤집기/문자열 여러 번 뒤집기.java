class Solution {
    public String solution(String my_string, int[][] queries) {
        String answer = "";
        StringBuffer ans_string = new StringBuffer(my_string);
        StringBuffer sb = new StringBuffer();
        
        for(int[] q : queries){
            sb.append(ans_string.substring(q[0], q[1]+1));
            ans_string.replace(q[0], q[1]+1, sb.reverse().toString());
            sb.setLength(0);
        }
        
        answer = ans_string.toString();
    
        return answer;
    }
}