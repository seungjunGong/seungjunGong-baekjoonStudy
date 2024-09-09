import java.util.*;
import java.util.regex.Pattern;

class Solution {
    
    public static int get_inter(List<String> aList, List<String> bList){
        int res = 0;
        String a, b;
        for(int i = 0; i < aList.size(); i++){
            a = aList.get(i);
            for(int j = 0; j < bList.size(); j++){
                b = bList.get(j);
                if(a.equals(b)){
                    res++;    
                    bList.remove(j);
                    break;
                }
            }
        }
        return res;
    }
    
    public int solution(String str1, String str2) {
        
        double answer = 0;
        
        List<String> aList = new ArrayList<>();
        List<String> bList = new ArrayList<>();
        
        String sub;
        for(int i = 0; i < str1.length()-1; i++){
            sub = str1.substring(i, i+2).toUpperCase();
            if(Pattern.matches("^[A-Z]*$", sub))
                aList.add(sub);            
        }
        for(int i = 0; i < str2.length()-1; i++){
            sub = str2.substring(i, i+2).toUpperCase();
            if(Pattern.matches("^[A-Z]*$", sub))
                bList.add(sub);            
        }
            
        double union = (double)aList.size() + (double)bList.size();
        int inter = (aList.size() > bList.size()) ? 
            get_inter(aList, bList) : get_inter(bList, aList);
        union -= inter;
        
		if(union == 0)
			answer = 1;	// 공집합일 경우 1
		else
			answer = (double) inter / (double) union;
        
        return (int)(answer * 65536);
    }
}