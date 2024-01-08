import java.util.*;

class Solution {
    public int[] solution(int[] progresses, int[] speeds) {
        int[] answer = {};
        List<Integer> ansList = new ArrayList<>();
        int days = 0, spend = 0, ans_i = -1;
        
        for(int i = 0; i < progresses.length; i++){
            spend = (int) Math.ceil((100.0 - progresses[i]) / speeds[i]);
            if(days >= spend){
                ansList.set(ans_i, ansList.get(ans_i) + 1);
            }else{
                days = spend;
                ansList.add(1);
                ans_i++;
            }
        }
        
        answer = ansList.stream().mapToInt(Integer::intValue).toArray();
        
        return answer;
    }
}