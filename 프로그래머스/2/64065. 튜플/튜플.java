import java.util.*;

class Solution {
    public int[] solution(String s) {
        int[] answer = {};
        
        Map<Integer, Integer> numCounts = new HashMap<>();
        int key = 0, value = 0;
        StringBuffer sb = new StringBuffer();
        String num_check = "{},";
        
        // 숫자 출현 횟수 카운트
        for(int i = 0; i < s.length(); i++){
            if(num_check.contains(String.valueOf(s.charAt(i)))){
                if(sb.length() > 0){
                    key = Integer.valueOf(sb.toString());
                    value = numCounts.getOrDefault(key, 0) + 1;
                    numCounts.put(key, value);
                    sb.setLength(0);
                }
            } else{
                sb.append(String.valueOf(s.charAt(i)));
            }
        }
        
        // 출현 횟수 순으로 내림차순 정렬
        answer = numCounts.entrySet().stream()
            .sorted(Map.Entry.comparingByValue(Collections.reverseOrder()))
            .mapToInt(Map.Entry::getKey)
            .toArray();
        
        
        return answer;
    }
}