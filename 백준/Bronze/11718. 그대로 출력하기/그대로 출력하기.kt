import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    while(true) {
        val line = readLine() ?: break
        println(line)
    }
}