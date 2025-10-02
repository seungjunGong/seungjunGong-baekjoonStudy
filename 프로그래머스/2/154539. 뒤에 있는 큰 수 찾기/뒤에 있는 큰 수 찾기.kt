import java.util.Stack

class Solution {
    fun solution(numbers: IntArray): IntArray {
        var answer: IntArray = IntArray(numbers.size) { -1 }
        
        val indexStack = Stack<Int>()
        
        for (i in numbers.indices) {
            while (indexStack.isNotEmpty() 
                   && numbers[indexStack.peek()] < numbers[i]) {
                val peekIndex = indexStack.pop()
                answer[peekIndex] = numbers[i] 
            }    
            indexStack.push(i)
        }
        
        return answer
    }
}