import java.time.LocalTime
import java.time.Duration
import kotlin.math.ceil

class Solution {
    fun solution(fees: IntArray, records: Array<String>): IntArray { 
        val recordMap = mutableMapOf<String, MutableList<LocalTime>>()
       
        records.forEach { record ->
            val (time, carNum, _) = record.split(" ")
            recordMap.getOrPut(carNum) { mutableListOf() }.add(LocalTime.parse(time))
        }
       
        return recordMap.toSortedMap().map { (_, times) ->
            val totalMinutes = times
                .let {if (it.size % 2 != 0) it + LocalTime.of(23, 59) else it}
                .chunked(2)
                .sumOf { (inTime, outTime) -> Duration.between(inTime, outTime).toMinutes() }
            if (totalMinutes <= fees[0]) fees[1]
            else fees[1] + ceil((totalMinutes - fees[0]) / fees[2].toDouble()).toInt() * fees[3]
       }.toIntArray()
    }
}