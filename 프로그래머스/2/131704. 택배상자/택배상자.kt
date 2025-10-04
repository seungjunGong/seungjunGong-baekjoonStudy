import java.util.Stack

class Solution {
    fun solution(order: IntArray): Int {
        var answer: Int = 0
        
        val subContainer = Stack<Int>()
        var orderIndex = 0
        
        for (box in 1..order.size) {
            subContainer.push(box)
            
            while(subContainer.isNotEmpty() && 
                    orderIndex < order.size &&
                    subContainer.peek() == order[orderIndex]) {
                subContainer.pop()
                answer++
                orderIndex++
            }
        }
        
        return answer
    }
}