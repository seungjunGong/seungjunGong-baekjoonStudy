import java.util.*;

class Solution {
    public int solution(String[] strArr) {
        int answer = 0;
        
        Map<Integer, Integer> lenCounts = new HashMap<>(strArr.length);
        
        for(String str: strArr){
            if(lenCounts.get(str.length()) == null)
                lenCounts.put(str.length(), 1);
            else
                lenCounts.put(str.length(),
                             lenCounts.get(str.length())+1);
        }
        
        answer = Collections.max(lenCounts.values());
        return answer;
    }
}