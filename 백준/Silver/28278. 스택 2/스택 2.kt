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
        
        when(command) {
            1 -> stack.addLast(st.nextToken().toInt())
            2 -> {
                val res = if (stack.isEmpty()) -1 else stack.removeLast()
                sb.append(res).append("\n")
            }
            3 -> sb.append(stack.size).append("\n")
            4 -> {
                val res = if (stack.isEmpty()) 1 else 0
                sb.append(res).append("\n")
            }
            5 -> {
                val res = stack.lastOrNull() ?: -1
                sb.append(res).append("\n")
            }
        }
    }
    print(sb)
}