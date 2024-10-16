import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, sum, max, min, num;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            sum = 0; min = 10000; max = 0;

            for(int i = 0; i < 10; i++){
                num = sc.nextInt();
                sum += num;
                min = Math.min(min, num); max = Math.max(max, num);
            }

            System.out.println("#" + test_case + " " + String.format("%.0f", (double)(sum-max-min)/8.0));
        }
    }
}