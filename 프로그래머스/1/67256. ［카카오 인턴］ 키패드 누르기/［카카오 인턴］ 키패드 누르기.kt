import kotlin.math.abs

class Solution {
    fun solution(numbers: IntArray, hand: String): String {
        var answer = ""
        
        val posMap = mutableMapOf<Int, Pair<Int, Int>>()
        arrayOf(
            intArrayOf(1, 2, 3),
            intArrayOf(4, 5, 6),
            intArrayOf(7, 8, 9),
            intArrayOf(10, 0, 11) // 10:*, 11:#
        ).forEachIndexed { r, row ->
            row.forEachIndexed { c, num ->
                posMap[num] = r to c
            }
        }
        
        var leftPos = posMap[10]!!
        var rightPos = posMap[11]!!
        
        numbers.forEach { number ->
            posMap[number]?.let { pos ->
                when(number) {
                    1, 4, 7 -> { // 왼쪽 키패드
                        answer += "L"
                        leftPos = pos
                    }
                    3, 6, 9 -> { // 오른쪽 키패드
                        answer += "R"
                        rightPos = pos
                    }
                    else -> {
                        val leftDist = abs(leftPos.first - pos.first) + abs(leftPos.second - pos.second)
                        val rightDist = abs(rightPos.first - pos.first) + abs(rightPos.second - pos.second)
                        
                        if (leftDist < rightDist) {
                            answer += "L"
                            leftPos = pos
                        } else if (leftDist > rightDist) {
                            answer += "R"
                            rightPos = pos
                        } else {
                            if (hand == "right") {
                                answer += "R"
                                rightPos = pos
                            } else {
                                answer += "L"
                                leftPos = pos
                            }
                        }
                    }
                }
            }
        }

        return answer
    }
}