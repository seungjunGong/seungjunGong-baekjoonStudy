private val br = System.`in`.bufferedReader()
private val bw = System.out.bufferedWriter()

fun main() {
    val stack = ArrayDeque<Int>()
    
    val N = br.readLine().toInt()
    
    repeat(N) {
        val commends = br.readLine().split(" ") 
        
        when (commends[0]) {
            "push" -> stack.addLast(commends[1].toInt())
            "pop" -> bw.write("${stack.removeLastOrNull() ?: -1}\n")
            "size" -> bw.write("${stack.size}\n")
            "empty" -> {
                if (stack.isEmpty()) bw.write("1\n")
                else bw.write("0\n")
            }
            "top" -> bw.write("${stack.lastOrNull() ?: -1}\n")
        }
    }
    bw.close()
}