class Solution {
    public int solution(int[] nums) {
        int answer = 0;
    
        int sum;
        int i;
        for(int a = 0; a < nums.length-2; a++){
            for(int b = a+1; b < nums.length-1; b++){
                for(int c = b+1; c < nums.length; c++){
                    sum = nums[a]+nums[b]+nums[c];
                    for(i = 2; i < sum; i++){
                        if(sum % i == 0) break;
                    }
                    if(i == sum) answer++;
                }
            }
        }

        return answer;
    }
}