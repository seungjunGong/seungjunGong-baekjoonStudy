// 풀이X
class Solution {        
    
    int dfs(int n, int plusCnt){
        
        /* 앞으로 나올 *의 개수 => 3을 몇번 곱해야 하는 지?
           반드시 나와야할 * 최소 개수 => 홀수개를 포함하여 2로 나눈 개수
        */
        if(Math.log(n)/Math.log(3) < (plusCnt+1) / 2)
            return 0;
        
        if(n==3 && plusCnt==2)
            return 1;
        
        int res = 0;
        if(n%3 == 0 && plusCnt >= 2)
            res += dfs(n/3, plusCnt-2);
        res += dfs(n-1, plusCnt+1);
        
        return res;
    }
    
    public int solution(int n) {
        return dfs(n-2, 2);
    }
}