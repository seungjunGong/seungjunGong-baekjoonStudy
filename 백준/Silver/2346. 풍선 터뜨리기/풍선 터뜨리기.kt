import java.io.BufferedReader
import java.io.InputStreamReader
import java.util.StringTokenizer

data class Balloon(
    val index: Int,
    val move: Int
)

fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    val st = StringTokenizer(readLine())

    val balloons = mutableListOf<Balloon>()
    for (i in 1..n) {
        balloons.add(Balloon(i, st.nextToken().toInt()))
    }

    val sb = StringBuilder()
    var currentIndex = 0

    while (balloons.isNotEmpty()) {
        val current = balloons.removeAt(currentIndex)
        sb.append(current.index).append(' ')

        if (balloons.isEmpty()) break

        currentIndex = if (current.move > 0) {
            (currentIndex + current.move - 1) % balloons.size
        } else {
            (currentIndex + current.move) % balloons.size
        }

        if (currentIndex < 0) currentIndex += balloons.size
    }

    print(sb)
}

/* 메모리 초과 4MB 
fun main() = with(BufferedReader(InputStreamReader(System.`in`))) {
    val n = readLine().toInt()
    
    val st = StringTokenizer(readLine())
    val deque = ArrayDeque<Pair<Int, Int>>()
    
    for (i in 1..n) { deque.addLast(i to st.nextToken().toInt()) }
    
    val sb = StringBuilder()
    while (deque.isNotEmpty()) {
        val (num, move) = deque.removeFirst()
        sb.append(num).append(' ')
        
        if (deque.isEmpty()) break // 마지막인 경우, 회전 x
        
        var moveCount = move
        while (moveCount > 1) {
            deque.addLast(deque.removeFirst())
            moveCount--
        }
        
        while (moveCount < 0) {
            deque.addFirst(deque.removeLast())
            moveCount++    
        }
    }
    print(sb)
}
*/