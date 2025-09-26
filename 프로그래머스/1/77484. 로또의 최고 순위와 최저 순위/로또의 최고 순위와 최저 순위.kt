class Solution {
    val MAX_SIZE = 6
    
    fun solution(lottos: IntArray, win_nums: IntArray): IntArray {
        var correctCounts = 0
        var zeroCounts = 0 
        
        lottos.forEach { lotto ->
            if (lotto == 0) {
                zeroCounts += 1        
            } else {
                if (lotto in win_nums) {
                    correctCounts += 1
                }
            }
        }
        
        val bestRank = (MAX_SIZE - zeroCounts - correctCounts + 1).coerceAtMost(6)
        val worstRank = (MAX_SIZE - correctCounts + 1).coerceAtMost(6)
        
        val answer: IntArray = intArrayOf(bestRank, worstRank)    
        return answer
    }
}