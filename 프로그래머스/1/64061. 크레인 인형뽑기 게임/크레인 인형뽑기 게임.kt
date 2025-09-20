class Solution {
    fun insertItemToBasket(item: Int, basket: MutableList<Int>): Boolean {
        val lastIndex = basket.lastIndex
        if (item == basket[lastIndex]) {
            basket.removeAt(lastIndex)
            return false
        } 
        basket.add(item)
        return true
    }
    
    fun solution(board: Array<IntArray>, moves: IntArray): Int {
        var answer = 0
        
        var basketList = mutableListOf(0)
        
        for (move in moves) {
            val col = move - 1
            for (i in 0 until board.size) {
                if (board[i][col] != 0) {
                    if(!insertItemToBasket(board[i][col], basketList)) {
                        answer += 2
                    }
                    board[i][col] = 0
                    break
                }
            }    
        }   
        
        return answer
    }
}