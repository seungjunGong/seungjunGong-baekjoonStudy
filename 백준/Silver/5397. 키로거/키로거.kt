private val br = System.`in`.bufferedReader()
private val bw = System.out.bufferedWriter()

fun main() {
    val T = br.readLine().toInt()
    val sb = StringBuilder()
    
    repeat(T) {
        val left = ArrayDeque<Char>()
        val right = ArrayDeque<Char>()
        val inputValue = br.readLine()
        
        for (c in inputValue) {
            when (c) {
                '<' -> if (left.isNotEmpty()) right.addFirst(left.removeLast())
                '>' -> if (right.isNotEmpty()) left.addLast(right.removeFirst())
                '-' -> if (left.isNotEmpty()) left.removeLast()
                else -> left.addLast(c)
            }
        }
        for (c in left) sb.append(c)
        for (c in right) sb.append(c)
        sb.append('\n')
    }
    bw.write("$sb")
    bw.close()
    
}