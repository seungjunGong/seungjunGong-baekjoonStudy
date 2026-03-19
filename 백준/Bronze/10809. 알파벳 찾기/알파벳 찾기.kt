import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val st = StringTokenizer(readLine())
    val s = st.nextToken()
    
    val pos = IntArray(26) { -1 }
    
    for (i in s.indices) {
        val c = (s[i].code - 97)     // ASCII Code 의 인덱스로 매핑
        if (pos[c] == -1) pos[c] = i // 처음 방문 위치 저장 
    }
    
    print(pos.joinToString(" "))
}