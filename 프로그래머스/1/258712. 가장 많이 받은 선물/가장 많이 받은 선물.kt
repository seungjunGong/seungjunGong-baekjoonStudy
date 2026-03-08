class Solution {
    fun solution(friends: Array<String>, gifts: Array<String>): Int {
        val mapping = mutableMapOf<String, Int>()
        val n = friends.size
        val giftRecords = Array(n) { IntArray(n) }
        val giftScore = IntArray(n)
        val nextGiftCounts = IntArray(n)
        
        friends.forEachIndexed { index, friend ->
            mapping[friend] = index
        }
        
        gifts.forEach { gift ->
            val (a, b) = gift.split(" ")
            val (giver, receiver) = mapping[a]!! to mapping[b]!!
            giftRecords[giver][receiver] += 1
            giftScore[giver] += 1
            giftScore[receiver] -= 1
        }
        
        for (i in 0 until n) {
            for (j in i + 1 until n) {
                if (giftRecords[i][j] > giftRecords[j][i]) {
                    nextGiftCounts[i] += 1
                } else if (giftRecords[i][j] < giftRecords[j][i]) {
                    nextGiftCounts[j] += 1
                } else {
                    if (giftScore[i] > giftScore[j]) {
                        nextGiftCounts[i] += 1
                    } else if (giftScore[i] < giftScore[j]) {
                        nextGiftCounts[j] += 1
                    }
                }
            }
        }
        
        
        return nextGiftCounts.maxOrNull()!!
    }
}