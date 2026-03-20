import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val stack = ArrayDeque<Int>()
    val sb = StringBuilder()
    
    repeat(n) {
        val st = StringTokenizer(readLine())
        val command = st.nextToken().toInt()
        
        val output = when(command) {
            1 -> { stack.addLast(st.nextToken().toInt()); null }
            2 -> if (stack.isEmpty()) -1 else stack.removeLast()
            3 -> stack.size
            4 -> if (stack.isEmpty()) 1 else 0
            5 -> stack.lastOrNull() ?: -1
            else -> null
        }
        if (output != null) sb.append(output).append('\n')
    }
    print(sb)
}