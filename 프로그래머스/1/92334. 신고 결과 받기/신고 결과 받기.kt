class Solution {
    fun solution(id_list: Array<String>, report: Array<String>, k: Int): IntArray {
       
        val userReportMap = hashMapOf<String, MutableSet<String>>()
        report.forEach {
            val (userId, reportId) = it.split(" ")            
            userReportMap.getOrPut(userId) { mutableSetOf() }.add(reportId)
        }
        
        val reportCounts = userReportMap.values.flatten().groupingBy { it }.eachCount()

        val suspendedIds = reportCounts.filter { it.value >= k }.keys

        val answer = id_list.map { userId ->
            userReportMap.getOrDefault(userId, mutableSetOf()).count { reportId ->
                reportId in suspendedIds
            }
        }.toIntArray()
        
        return answer
    }
}