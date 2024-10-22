import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, money, wi;
        T=sc.nextInt();

        int[] won = new int[]{50000, 10000, 5000,
                            1000, 500, 100, 50, 10};
        for(int test_case = 1; test_case <= T; test_case++){
            money=sc.nextInt();

            System.out.println("#"+test_case);
            for(int i = 0; i < 8; i++){
                System.out.print(money/won[i] + " ");
                money %= won[i];
            }
            System.out.println();
        }
    }
}