class Solution {
    private val allNumbers = HashSet<Int>()
    private lateinit var isPrimeArray: BooleanArray
    private lateinit var charNumbers: CharArray
    private lateinit var visited: BooleanArray
    
    private val MAX_N = 10_000_000
    
    fun solution(numbers: String): Int {
        charNumbers = numbers.toCharArray()
        visited = BooleanArray(charNumbers.size)
            
        initIsPrime(MAX_N)
        
        dfs("")
        
        return allNumbers.count { isPrimeArray[it] }
    }
    
    private fun dfs(currentNum: String) {
        if (currentNum.isNotEmpty()) {
            allNumbers.add(currentNum.toInt())
        }
        
        for (i in charNumbers.indices) {
            if (!visited[i]) {
                visited[i] = true
                
                dfs(currentNum + charNumbers[i])
                
                visited[i] = false
            }
        }
    }
    
    private fun initIsPrime(n: Int) {
        isPrimeArray = BooleanArray(n+1) { true }
        
        isPrimeArray[0] = false
        isPrimeArray[1] = false
        
        var i = 2
        while (i * i <= n) {
            if (isPrimeArray[i]) {
                var j = i * i
                while (j <= n) {
                    isPrimeArray[j] = false
                    j += i
                }
            }
            i++
        }
    }
}