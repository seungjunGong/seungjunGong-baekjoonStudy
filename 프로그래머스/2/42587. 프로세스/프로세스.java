import java.util.*;

class Solution {
    
    boolean check_priority(List<Integer> list){
    for(int i = 1; i < list.size(); i++)
        if(list.get(i) > list.get(0))
            return false;
    return true;
    }
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        
        List<Integer> queue = new ArrayList<>();
        for(int p : priorities)
            queue.add(p);
        
        while(true){
            if(check_priority(queue)){
                answer++;
                if(location == 0)
                    break;   
                else
                    queue.remove(0);                    
            }else{
                queue.add(queue.remove(0));
            }
            location = (location + queue.size() - 1) % queue.size();
        }
        
        
        return answer;
    }
}