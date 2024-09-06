class Solution {
    
    boolean visited[];
    
    int dfs(int k, int[][] dg){
        int res = 0;
        for(int i = 0; i < dg.length; i++){
            if(!visited[i]) {
                visited[i] = true;
                if(k-dg[i][0] >= 0)
                  res = Math.max(res, dfs(k-dg[i][1], dg)+1);
                visited[i] = false;
            }   
        }      
        return res;
    }
    
    public int solution(int k, int[][] dungeons) {
        int answer = -1;
        
        visited = new boolean[dungeons.length];
        for(int i = 0; i < dungeons.length; i++)
            visited[i] = false;
        
        answer = dfs(k, dungeons);
        return answer;
    }
}