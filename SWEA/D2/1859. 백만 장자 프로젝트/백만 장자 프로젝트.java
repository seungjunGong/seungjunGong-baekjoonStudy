import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N, maxN;
        long M;
        T=sc.nextInt();

        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt();
            int[] arr = new int[N];

            for(int i = 0; i < N; i++){
                arr[i] = sc.nextInt();
            }

            M = 0; maxN = arr[N-1];
            for(int i = N-2; i >= 0; i--){
                if(maxN > arr[i]){
                   M += maxN - arr[i];
                }
                maxN = Math.max(maxN, arr[i]);
            }

            System.out.println("#" + test_case + " " + M);
        }
    }
}