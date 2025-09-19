class Solution {
    fun solution(n: Int, lost: IntArray, reserve: IntArray): Int {
        var answer = 0
        
        var totals = mutableListOf<Int>()
        
        for (i in 0..n-1)
            totals.add(1)
            
        for (index in lost)
            totals[index-1] -= 1
        
        for (index in reserve)
            totals[index-1] += 1
        
        for (i in 0..n-1) {
            if (totals[i] == 0) {
                if (i > 0 && totals[i-1] > 1) {
                    totals[i-1] -= 1
                    totals[i] += 1
                } else if (i < n-1 && totals[i+1] > 1) {
                    totals[i+1] -= 1
                    totals[i] += 1
                }
            }
            
            if (totals[i] > 0) {
                answer += 1
            }
        }
        
        return answer
    }
}