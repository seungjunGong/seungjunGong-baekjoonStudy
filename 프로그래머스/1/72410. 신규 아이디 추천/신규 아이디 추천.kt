class Solution {
    fun solution(new_id: String): String {
        var answer: String = ""
        
        val step1 = new_id.lowercase()
        val step2 = step1.replace(Regex("[^a-z0-9\\-_.]"), "")
        val step3 = step2.replace(Regex("\\.{2,}"), ".")
        val step4 = step3.trim('.')
        val step5 = if(step4.isEmpty()) "a" else step4
        val step6 = if (step5.length >= 16) step5.take(15).trimEnd('.') else step5
        val step7 = if (step6.length <= 2) step6.padEnd(3, step6.last()) else step6
        
        answer = step7
        return answer
    }
}