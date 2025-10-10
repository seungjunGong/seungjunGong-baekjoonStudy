class Solution {
    lateinit var arr: Array<IntArray>
    
    fun solution(arr: Array<IntArray>): IntArray {
        this.arr = arr
        
        val (zeros, ones) = compress(0, 0, arr.size)
        
        return intArrayOf(zeros, ones)
    }
    
    fun compress(r: Int, c: Int, size: Int): Pair<Int, Int> {
        if (checkSame(r, c, size)) {
            return if (arr[r][c] == 0) Pair(1, 0) else Pair(0, 1)
        }
        
        val newSize = size / 2
        val s1 = compress(r, c, newSize)
        val s2 = compress(r, c + newSize, newSize)
        val s3 = compress(r + newSize, c, newSize)
        val s4 = compress(r + newSize, c + newSize, newSize)
        
        val totalZeros = s1.first+ s2.first + s3.first + s4.first
        val totalOnes = s1.second + s2.second + s3.second + s4.second
        
        return Pair(totalZeros, totalOnes)
    }
    
    fun checkSame(r: Int, c: Int, size: Int): Boolean {
        val initValue = arr[r][c]
        
        for (i in r until r + size) {
            for (j in c until c + size) {
                if (arr[i][j] != initValue) {
                    return false
                }
            }
        }
        
        return true
    }
}