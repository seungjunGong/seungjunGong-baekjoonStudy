import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val deque = ArrayDeque<Int>()
    
    val sb = StringBuilder()
    repeat(n) {
        val st = StringTokenizer(readLine())
        val command = st.nextToken().toInt()
        
        val output = when(command) {
            1 -> { deque.addFirst(st.nextToken().toInt()); null }
            2 -> { deque.addLast(st.nextToken().toInt()); null }
            3 -> if (deque.isEmpty()) -1 else deque.removeFirst()
            4 -> if (deque.isEmpty()) -1 else deque.removeLast()
            5 -> deque.size
            6 -> if (deque.isEmpty()) 1 else 0
            7 -> deque.firstOrNull() ?: -1
            8 -> deque.lastOrNull() ?: -1
            else -> null
        }
        
        if (output != null) sb.append(output).append('\n')
    }
    print(sb)
}