import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    val reversedA = st.nextToken().reversed().toInt()
    val reversedB = st.nextToken().reversed().toInt()
    
    print(if (reversedA > reversedB) reversedA else reversedB)
}