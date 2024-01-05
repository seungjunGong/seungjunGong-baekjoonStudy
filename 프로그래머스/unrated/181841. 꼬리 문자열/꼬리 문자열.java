class Solution {
    public String solution(String[] str_list, String ex) {
        StringBuilder sb = new StringBuilder();
        String answer = "";
        
        for(String str: str_list)
            if(!str.contains(ex))
                sb.append(str);
        
        answer = sb.toString();
        return answer;
    }
}