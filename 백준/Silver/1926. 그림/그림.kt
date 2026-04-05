import java.util.StringTokenizer

val br = System.`in`.bufferedReader()
val bw = System.out.bufferedWriter()

fun main() {
    val (n, m) = br.readLine().split(" ").map { it.toInt() }
    val board = Array(n) { IntArray(m) }  
    
    for (i in 0 until n) {
        val st = StringTokenizer(br.readLine())
        for (j in 0 until m) {
            board[i][j] = st.nextToken().toInt()
        }
    }
    
    var drawingCount = 0
    var maxArea = 0
    for (i in 0 until n) {
        for (j in 0 until m) {
            if (board[i][j] == 1) {
                val area = getDrawingArea(board, i, j)
                drawingCount++
                maxArea = maxOf(area, maxArea)
            }
        }
    }
    
    bw.write("${drawingCount}\n${maxArea}")
    bw.close()
}

fun getDrawingArea(
    board: Array<IntArray>,
    row: Int,
    col: Int,
): Int {
    val (n, m) = board.size to board[0].size
    if (row < 0 || row >= n || col < 0 || col >= m) return 0
    if (board[row][col] == 0) return 0
    
    board[row][col] = 0
    
    return 1 +
        getDrawingArea(board, row + 1, col) +
        getDrawingArea(board, row - 1, col) +
        getDrawingArea(board, row, col + 1) +
        getDrawingArea(board, row, col - 1)
}