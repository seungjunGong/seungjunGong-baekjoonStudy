import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    
    var count = 0
    while (st.hasMoreTokens()) {
        st.nextToken()
        count++
    }
    print(count)
}