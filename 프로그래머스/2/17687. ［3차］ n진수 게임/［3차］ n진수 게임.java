import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        String answer = "";
        
        String nums = "";
        
        int current = 0;
        for(int i = 0; t > 0; i++){
            nums = Integer.toString(i, n).toUpperCase();
            
            for(int j = 0; j < nums.length(); j++){
                current++;
                if(p==current){
                    answer += nums.substring(j, j+1);
                    p += m;
                    t--;
                    if(t <= 0) break;
                }
            }
        }
        
        return answer;
    }
}