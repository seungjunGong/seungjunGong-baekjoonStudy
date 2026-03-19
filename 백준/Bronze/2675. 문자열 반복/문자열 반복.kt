import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val t = readLine().toInt()
    
    repeat(t) {
        val st = StringTokenizer(readLine())
        val r = st.nextToken().toInt()
        val s = st.nextToken()
        
        val sb = StringBuilder()
        for (c in s) sb.append(c.toString().repeat(r)) // 문자 r 번 반복
        
        println(sb)
    }
}