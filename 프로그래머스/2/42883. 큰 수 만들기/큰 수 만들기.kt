class Solution {
    fun solution(number: String, k: Int): String {
        var answer = StringBuilder(number.length)
        
        var remove = k
        
        for (c in number) {
            while (remove > 0 && answer.isNotEmpty() && answer.last() < c) {
                answer.deleteCharAt(answer.length - 1)
                remove--
            }
            answer.append(c)
        }
        
        if (remove > 0) answer.setLength(answer.length - remove)
        
        return answer.toString()
    }
}