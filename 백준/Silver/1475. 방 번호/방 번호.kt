import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val s = readLine()
    val numbers = IntArray(10)
    
    for (w in s) {
        val i = w - '0'
        numbers[i] += 1
    }
    
    numbers[6] = (numbers[6] + numbers[9] + 1) / 2
    numbers[9] = 0
    
    print(numbers.maxOrNull())
}