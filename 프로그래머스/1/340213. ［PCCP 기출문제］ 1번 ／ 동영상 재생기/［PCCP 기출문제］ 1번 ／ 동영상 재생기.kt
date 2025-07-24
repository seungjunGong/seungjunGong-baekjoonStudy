class Solution {
    fun String.toSeconds(): Int {
        val (min, sec) = this.split(":").map { it.toInt() }
        return min * 60 + sec
    }
    
    fun solution(video_len: String, pos: String, op_start: String, op_end: String, commands: Array<String>): String {
        val (opStartSec, opEndSec) = op_start.toSeconds() to op_end.toSeconds()
        val videoLenSec = video_len.toSeconds()
        var currentSec = pos.toSeconds()
        
        for (command in commands){
            if (currentSec in opStartSec..opEndSec)
                currentSec = opEndSec       
            
            currentSec += if (command == "prev") (-10) else 10
            currentSec = currentSec.coerceIn(0, videoLenSec)
        }
        
        if (currentSec in opStartSec..opEndSec)
            currentSec = opEndSec       
    
        return "%02d:%02d".format(currentSec / 60, currentSec % 60)
    }
}