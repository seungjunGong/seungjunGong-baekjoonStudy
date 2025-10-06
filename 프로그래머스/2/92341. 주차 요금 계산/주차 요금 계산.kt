import java.time.LocalTime
import java.time.Duration

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray { 
        var answer: IntArray = intArrayOf()
    
        val recordMap = mutableMapOf<String, MutableList<LocalTime>>()
        
        records.forEach { r ->
            val (time, carNum, status) = r.split(" ")
            val localTime = LocalTime.parse(time)
            recordMap.getOrPut(carNum) { mutableListOf() }.add(localTime)
        }
        
        val result = mutableListOf<Int>()
        for (times in recordMap.toSortedMap().values) {
            var totalMinutes = 0L
            val timeLine = if (times.size % 2 != 0) 
                times + listOf(LocalTime.of(23, 59)) 
            else times
            
            for (i in timeLine.indices step 2) {
                val (inTime, outTime) = Pair(timeLine[i], timeLine[i + 1])
                val duration = Duration.between(inTime, outTime).toMinutes()
                totalMinutes += duration
            }
            val addFee = Math.ceil(Math.max(0, totalMinutes - fees[0]) / fees[2].toDouble()).toInt()
            result.add(fees[1] + addFee * fees[3])
        }
            
        answer = result.toIntArray()
        return answer
    }
}