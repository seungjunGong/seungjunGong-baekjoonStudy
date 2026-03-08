// version repactoring
class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val n = friends.size
        val nameToIndex = mutableMapOf<String, Int>()
        val giftHistory = Array(n) { IntArray(n) }
        val giftBalance = IntArray(n) // 준 수 - 받은 수
        val nextReceivedCount = IntArray(n)
        
        friends.forEachIndexed { index, friend ->
            nameToIndex[friend] = index
        }
        
        gifts.forEach { gift ->
            val (giverName, receiverName) = gift.split(" ")
            val giver = nameToIndex[giverName]!!
            val receiver = nameToIndex[receiverName]!!
            
            giftHistory[giver][receiver] += 1
            giftBalance[giver] += 1
            giftBalance[receiver] -= 1
        }
        
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                val iToJ = giftHistory[i][j]
                val jToI = giftHistory[j][i]
                
                if (iToJ > jToI) {
                    nextReceivedCount[i]++
                } else if (iToJ < jToI) {
                    nextReceivedCount[j]++
                } else {
                    if (giftBalance[i] > giftBalance[j]) {
                        nextReceivedCount[i]++
                    } else if (giftBalance[i] < giftBalance[j]) {
                        nextReceivedCount[j]++
                    }
                }
            }
        }
        
        return nextReceivedCount.maxOrNull()!!
    }
}