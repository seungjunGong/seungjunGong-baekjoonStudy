class Solution {
    fun solution(x: Int, y: Int, n: Int): Int {
        var answer: Int = 0
        val xList = MutableList(y + 1) { 1000000 }

        xList[x] = 0
        for (i in x..y) {
            if (xList[i] >= 0 && xList[i] < 1000000) {
                if (i + n <= y && xList[i + n] > xList[i] + 1) {
                    xList[i + n] = xList[i] + 1
                }
                if (i * 2 <= y && xList[i * 2] > xList[i] + 1) {
                    xList[i * 2] = xList[i] + 1 
                }
                if (i * 3 <= y && xList[i * 3] > xList[i] + 1) {
                    xList[i * 3] = xList[i] + 1
                }
            }
        }
        
        answer = if (xList[y] == 1000000) -1 else xList[y]
        
        return answer
    }
}