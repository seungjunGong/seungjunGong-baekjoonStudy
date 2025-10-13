import java.util.ArrayDeque

class Solution {
    fun solution(queue1: IntArray, queue2: IntArray): Int {
        var answer = 0
        
        val q1 = ArrayDeque<Long>()
        val q2 = ArrayDeque<Long>()
        
        var sum1 = 0L
        var sum2 = 0L
        
        for (i in queue1.indices) {
            val tmp1 = queue1[i].toLong()
            val tmp2 = queue2[i].toLong()
            q1.add(tmp1)
            q2.add(tmp2)
            sum1 += tmp1
            sum2 += tmp2
        }
        
        if ((sum1 + sum2) % 2 != 0L) {
            return -1
        }
        
        val limit = queue1.size * 4     // 모든 원소 순환 최대 횟수
            
        while (answer <= limit) {
            if (sum1 == sum2) {
                return answer
            }
            
            if (sum1 > sum2) {
                if (q1.isEmpty()) break 
                
                val tmp = q1.removeFirst()
                q2.add(tmp)
                sum1 -= tmp
                sum2 += tmp
            } else {
                if (q2.isEmpty()) break 
                
                val tmp = q2.removeFirst()
                q1.add(tmp)
                sum1 += tmp
                sum2 -= tmp
            }
            answer++
        } 
        
        return -1
    }
}