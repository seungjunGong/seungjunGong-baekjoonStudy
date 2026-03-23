import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val left = ArrayDeque<Char>()
    val right = ArrayDeque<Char>()
    val str = readLine()
    str.forEach { c ->
        left.addLast(c)
    }
    
    val m = readLine().toInt()
    
    repeat(m) {
        val st = StringTokenizer(readLine())
        val commend = st.nextToken()
        
        when(commend) {
            "L" -> if (left.isNotEmpty()) right.addFirst(left.removeLast())
            "D" -> if (right.isNotEmpty()) left.addLast(right.removeFirst())
            "B" -> if (left.isNotEmpty()) left.removeLast()
            "P" -> left.addLast(st.nextToken()[0])
        }
    }
    
    val result = StringBuilder()
    for (c in left) result.append(c)
    for (c in right) result.append(c)
    print(result)
}