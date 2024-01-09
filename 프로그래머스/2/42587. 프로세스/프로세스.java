import java.util.*;

class Solution {
    
    public int solution(int[] priorities, int location) {
        int answer = 0;
        int peek = 0;
            
        List<Integer> queue = new ArrayList<>();
        for(int p : priorities)
            queue.add(p);
        
        Arrays.sort(priorities); // idea -> 정렬을 수행 했을 때 첫번 째 값만 비교하면 
                                 // 나머지 값은 전부 우선순위가 작으므로 비교할 필요가 없다.
        
        int size = priorities.length - 1;
        while(!queue.isEmpty()){
            peek = queue.remove(0);
            if(peek == priorities[size - answer]){ // 우선순위가 가장 높은 경우
                answer++;
                if(location == 0)
                    break;   
            }else{                                 // 우선 순위가 높은 것이 있는 경우
                queue.add(peek);
            }
            location = (location + queue.size() - 1) % queue.size();
        }
        
        return answer;
    }
}