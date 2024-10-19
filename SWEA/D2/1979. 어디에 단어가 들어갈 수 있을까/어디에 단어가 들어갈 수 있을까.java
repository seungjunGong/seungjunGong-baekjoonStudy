import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N, K, ans, row, col;

        T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++){
            N=sc.nextInt(); K=sc.nextInt();

            int[][] puzzle = new int[N][N];
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    puzzle[i][j] = sc.nextInt();
                }
            }

            ans = 0;
            for(int i = 0; i < N; i++){
                col = 0; row = 0;
                for(int j = 0; j < N; j++){
                    if(puzzle[i][j] == 1)
                        row++;
                    else {
                        if(row == K) ans++;
                        row=0;
                    }
                    if(puzzle[j][i] == 1)
                        col++;
                    else{
                        if(col==K) ans++;
                        col=0;
                    }
                }
                if(row==K) ans++;
                if(col==K) ans++;
            }
            System.out.println("#"+test_case+" "+ans);
        }
    }
}