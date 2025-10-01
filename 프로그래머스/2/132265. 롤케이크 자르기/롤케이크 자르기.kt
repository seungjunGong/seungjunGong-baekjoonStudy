class Solution {
    fun solution(topping: IntArray): Int {
        var answer: Int = 0
        
        val leftMap = mutableMapOf<Int, Int>()
        topping.forEach { t ->
            leftMap[t] = leftMap.getOrDefault(t, 0) + 1
        }
        val rightMap = mutableMapOf<Int, Int>()
        
        for (t in topping) {
            rightMap[t] = rightMap.getOrDefault(t, 0) + 1
            
            leftMap[t] = leftMap.getOrDefault(t, 0) - 1
            if (leftMap[t] == 0) {
                leftMap.remove(t)
            }
            
            if (leftMap.size == rightMap.size) {
                answer++
            }
        }
        
        return answer
    }
}