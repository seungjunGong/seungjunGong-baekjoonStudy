import java.util.Arrays;
class Solution {
    public String solution(String s) {
        String answer = "";
        int[] intArr = Arrays.stream(s.split(" "))
            .mapToInt(Integer::parseInt)
            .toArray();
        
        Arrays.sort(intArr);
        // 문자열 합치기 연산
        answer = intArr[0] + " " + intArr[intArr.length-1];
        
        return answer;
    }
}