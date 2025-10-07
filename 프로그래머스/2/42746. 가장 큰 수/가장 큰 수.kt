class Solution {
    fun solution(numbers: IntArray): String {
        var answer = ""
        val strs = numbers.map { it.toString() }

        val sorted = strs.sortedWith { a, b ->
            (b + a).compareTo(a + b)
        }

        if (sorted[0] == "0") return "0"
        
        return sorted.joinToString("")
    }
}