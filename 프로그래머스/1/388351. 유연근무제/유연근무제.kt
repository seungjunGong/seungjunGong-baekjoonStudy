class Solution {

    private fun toMinutes(timeVal: Int): Int {
        val hours = timeVal / 100
        val minutes = timeVal % 100
        return hours * 60 + minutes
    }

    fun solution(schedules: IntArray, timelogs: Array<IntArray>, startday: Int): Int {
        var answer: Int = 0
        
        for (i in schedules.indices) {
           val deadlineTime = toMinutes(schedules[i]) + 10
            
            var isSuccessful = true
            
            for (j in 0 until 7) {
                val currentDay = ((startday - 1 + j) % 7) + 1
                
                if (currentDay <= 5) {
                    val arrivalTime = toMinutes(timelogs[i][j])
                    
                    if (arrivalTime > deadlineTime) {
                        isSuccessful = false
                        break
                    }
                }
            }
            
            if (isSuccessful) {
                answer++
            }
        }
        return answer
    }
}