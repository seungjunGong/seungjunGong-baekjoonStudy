class Solution {
    fun isSolvableWithinTimeLimit(
        diffs: IntArray,
        times: IntArray,
        limit: Long,
        level: Int
    ): Boolean {
        var totalTime = 0L
        val n = diffs.size
        
        for (i in 0 until n) {
            val diff = diffs[i]
            val timeCur = times[i]
            
            if (diff <= level){
                totalTime += timeCur
            } else {
                val failCount = diff - level
                val timePrev = if (i > 0) times[i - 1] else 0   
                
                totalTime += (timeCur + timePrev).toLong() * failCount + timeCur
            }
            
            if (totalTime > limit) return false
        }
        return true
    }
    
    fun solution(
        diffs: IntArray,
        times: IntArray,
        limit: Long
    ): Int {
        val maxDiff = diffs.maxOrNull() ?: return 0
        var (low, high) = 1 to maxDiff
        
        while (low <= high) {
            val midLevel = (low + high) / 2
            
            if(isSolvableWithinTimeLimit(diffs, times, limit, midLevel)){
                high = midLevel - 1
            } else{
                low = midLevel + 1
            }
        }
        
        return low
    }
}