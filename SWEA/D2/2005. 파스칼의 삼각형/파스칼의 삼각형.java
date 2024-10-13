import java.util.*;
import java.io.FileInputStream;

/* 파스칼의 삼각형
*  nCr = n-1Cr-1 + n-1Cr
*  1
*  1C0 1C1
*  2C0 2C1 2C2
* */
class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N;
        T=sc.nextInt();

        int[][] comb = new int[11][11];
        for(int i = 0; i < 11; i++) // 초기화
            comb[i][0] = 1;

        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt();

            System.out.println("#" + test_case);
            for(int i = 0; i < N; i++){
                for(int j = 0; j <= i; j++){
                    if(comb[i][j] == 0){
                        comb[i][j] = comb[i-1][j-1] + comb[i-1][j];
                    }
                    System.out.print(comb[i][j] + " ");
                }
                System.out.println();
            }
        }
    }
}