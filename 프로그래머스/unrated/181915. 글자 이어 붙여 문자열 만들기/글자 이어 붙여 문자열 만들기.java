class Solution {
    public String solution(String my_string, int[] index_list) {
        StringBuilder sb = new StringBuilder();
        String answer = "";
        
        for(int i : index_list)
            sb.append(my_string.charAt(i));
        
        answer = sb.toString();
        return answer;
    }
}