import java.util.*;

class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        
        HashMap<String, Integer> checkList = new HashMap<>();
        
        for(String pt : participant){
            if(checkList.containsKey(pt))
                checkList.replace(pt, checkList.get(pt)+1);
            else
                checkList.put(pt, 1);
        }
        
        for(String cp : completion){
            checkList.replace(cp, checkList.get(cp)-1);
            
            if(checkList.get(cp) <= 0)
                checkList.remove(cp);
        }
        
        Iterator<String> keys = checkList.keySet().iterator();
        answer = keys.next();
        
        return answer;
    }
}