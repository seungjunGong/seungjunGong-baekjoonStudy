import java.util.*;

class Solution {
    public String[] solution(String myString) {
        String[] answer = {};
        List<String> strList = new ArrayList<>();
        StringBuilder buffer = new StringBuilder();
        
        for(int i = 0; i < myString.length(); i++){
            if(myString.charAt(i) == 'x'){
                if(buffer.length() > 0){
                    strList.add(buffer.toString());
                    buffer.setLength(0);
                }
            }
            else{
                buffer.append(myString.charAt(i));                
            }
        }
        
        if(buffer.length() > 0)
            strList.add(buffer.toString());
        
        Collections.sort(strList);
        answer = strList.toArray(new String[strList.size()]);
        return answer;
    }
}