import java.io.BufferedReader
import java.io.InputStreamReader

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val s = readLine()
    val dialTime = intArrayOf(3, 3, 3,
                              4, 4, 4,
                              5, 5, 5,
                              6, 6, 6,
                              7, 7, 7,
                              8, 8, 8, 8,
                              9, 9, 9,
                              10, 10, 10, 10
                      )
    
    var total = 0
    for (c in s) {
        val dialNum = c.code - 65
        total += dialTime[dialNum]
    }
    print(total)
}