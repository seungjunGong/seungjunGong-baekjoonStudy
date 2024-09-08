/*
    1번 1,2,3,4,5
    2번 2,1,2,3,2,4,2,5
    3번 3,3,1,1,2,2,4,4,5,5
*/
import java.util.*;

class Solution {
    public int[] solution(int[] answers) {
        List<Integer> ansList = new ArrayList<>();
        
        int supoja[][] = {{1,2,3,4,5}, 
                   {2,1,2,3,2,4,2,5}, 
                   {3,3,1,1,2,2,4,4,5,5}};
        
        int score[] = new int[3];
        int max_s = 0;
        int num;
        for(int i = 0; i < 3; i++){
            score[i] = 0;
            num = 0;
            
            for(int j = 0; j < answers.length; j++){
                if(supoja[i][num] == answers[j])
                    score[i]++;
                num = (num + 1) % supoja[i].length;        
            }
            max_s = Math.max(max_s, score[i]);
        }    
        
        for(int i = 0; i < 3; i++) {
            if(max_s == score[i])
                ansList.add(i+1);
        }
        
        int answer[] = new int[ansList.size()];
        for(int i = 0; i < answer.length; i++)
            answer[i] = ansList.get(i);
        
        return answer;
    }
}