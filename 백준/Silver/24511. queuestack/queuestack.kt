import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    
    var st = StringTokenizer(readLine())
    val queueStack = IntArray(n) { st.nextToken().toInt() }
    
    st = StringTokenizer(readLine())
    val arr = IntArray(n) { st.nextToken().toInt() }
    
    val queue = ArrayDeque<Int>()
    for (i in 0 until n) {
        if (queueStack[i] == 0) queue.addFirst(arr[i])
    }

    val m = readLine().toInt()
    st = StringTokenizer(readLine())
    val sb = StringBuilder()
    
    repeat(m) {
        val input = st.nextToken().toInt()
        
        queue.addLast(input)
        sb.append(queue.removeFirst()).append(' ')
    }
    
    print(sb)
}