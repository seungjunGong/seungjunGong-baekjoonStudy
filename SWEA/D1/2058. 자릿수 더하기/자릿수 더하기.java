import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int sum = 0;

        for(String s : sc.nextLine().split("")){
            sum += Integer.parseInt(s);
        }
        System.out.println(sum);
    }
}