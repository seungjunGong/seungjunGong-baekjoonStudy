import java.util.*;

class Solution {
    
    boolean is_prime(long n){
        if(n == 1) return false;
        
        for(int i = 2; i < (long)Math.sqrt(n)+1; i++){
            if(n % i == 0) return false;
        }
        return true;
    }
    
    public int solution(int n, int k) {
        int answer = 0;
        
        String sNums[] = Integer.toString(n, k).split("0");
        
        for(int i = 0; i < sNums.length; i++){
            if(!sNums[i].isEmpty() && is_prime(Long.parseLong(sNums[i])))
               answer++;                
        }
        
        return answer;
    }
}