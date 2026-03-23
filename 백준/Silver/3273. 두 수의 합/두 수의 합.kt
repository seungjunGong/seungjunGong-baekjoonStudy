import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    
    val st = StringTokenizer(readLine())
    val arr = IntArray(n) { st.nextToken().toInt() }
    arr.sort()
    
    val x = readLine().toInt()
    
    // 투포인터
    var left = 0
    var right = n - 1
    var count = 0
    while(left < right) {
        val sum = arr[left] + arr[right]
        
        when {
            sum == x -> {
                count++
                left++
                right-- // 같은 경우 증감
            }
            sum < x -> left++ // 값 증가
            else -> right--   // 값 감소
        }
    }
    print(count)
}