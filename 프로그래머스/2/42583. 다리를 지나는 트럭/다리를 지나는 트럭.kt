import java.util.ArrayDeque

class Solution {
    fun solution(bridge_length: Int, weight: Int, truck_weights: IntArray): Int {
        var time = 0
        
        val bridge = ArrayDeque(MutableList(bridge_length) { 0 })
        var currentWeight = 0
        var truckIdx = 0
        
        while (truckIdx < truck_weights.size) {
            time += 1
            currentWeight -= bridge.pollFirst()
            
            if (currentWeight + truck_weights[truckIdx] <= weight) {
                currentWeight += truck_weights[truckIdx]
                bridge.addLast(truck_weights[truckIdx++])
            } else {
                bridge.addLast(0)
            }
        }   
        
        time += bridge_length
        
        return time
    }
}