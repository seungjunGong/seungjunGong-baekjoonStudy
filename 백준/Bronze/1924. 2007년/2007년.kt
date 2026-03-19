import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    val x = st.nextToken().toInt()
    val y = st.nextToken().toInt()
    
    val monthOfDays = arrayOf("MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN")
    val day = intArrayOf(0, 31, 28, 31,
                         30, 31, 30,
                         31, 31, 30,
                         31, 30, 31)
    
    var total = y - 1 // 기본 요일: "MON" 따라서, -1
    for (i in 1 until x) {
        total += day[i]
    }
    
    println(monthOfDays[total % 7])
}