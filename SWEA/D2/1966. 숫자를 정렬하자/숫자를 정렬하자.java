import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++){
            N=sc.nextInt();

            int[] arr = new int[N];
            for(int i = 0; i < N; i++) arr[i]=sc.nextInt();
            Arrays.sort(arr); System.out.print("#" + test_case);
            for(int x : arr){ System.out.print(" " + x); }
            System.out.println();
        }
    }
}