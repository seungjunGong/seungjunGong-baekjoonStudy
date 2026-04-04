private val br = System.`in`.bufferedReader()
private val bw = System.out.bufferedWriter()

fun main() {
    val (N, K) = br.readLine().split(" ").map { it.toInt() }
    
    val visited = BooleanArray(N)
    
    val sb = StringBuilder()
    sb.append("<")
    var i = 0
    var count = 0
    var step = 0
    while (count < N) {
        val idx = i % N
        if (!visited[idx]) {
            if (step + 1 < K) {
                step++
            } else {
                visited[idx] = true

                if (count + 1 == N) {
                    sb.append("${idx+1}>")
                } else {
                    sb.append("${idx+1}, ")                
                }
                step = 0
                count++
            }
        }
        i++
    }
    bw.write("${sb}")
    bw.close()
}