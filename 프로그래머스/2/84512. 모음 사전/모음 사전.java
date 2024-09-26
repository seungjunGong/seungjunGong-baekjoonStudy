import java.util.*;

class Solution {
    
    static List<String> words = new ArrayList<>();
        
    void dfs(String st){
        if(st.length() > 5)
            return;
        
        words.add(st);
        
        for(int i = 0; i < 5; i++){
            dfs(st + "AEIOU".charAt(i));
        }
    }
    
    public int solution(String word) {
        int answer = 0;  
        
        dfs("");
        
        answer = words.indexOf(word);
        return answer;
    }
}