import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    
    val st = StringTokenizer(readLine())
    var currentNum = 1
    val stack = ArrayDeque<Int>()
    
    while(st.hasMoreTokens()) {
        val waitingNum = st.nextToken().toInt()
        
        if (currentNum == waitingNum) currentNum++ else stack.addLast(waitingNum)
        
        while (stack.safeLast() == currentNum) {
            stack.removeLast()
            currentNum++
        }
    }
    
    print(if (currentNum == n+1) "Nice" else "Sad")
}

private fun ArrayDeque<Int>.safeLast() = this.lastOrNull() ?: -1