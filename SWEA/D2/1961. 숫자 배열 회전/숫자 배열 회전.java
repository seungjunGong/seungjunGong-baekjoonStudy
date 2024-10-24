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

            int[][] arr = new int[N][N];
            String[][] res = new String[N][3];
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    arr[i][j] = sc.nextInt();
                }
                res[i][0]=""; res[i][1]=""; res[i][2]="";
            }

            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    res[i][0] += "" + arr[N-j-1][i];
                    res[i][1] += "" + arr[N-i-1][N-j-1];
                    res[i][2] += "" + arr[j][N-i-1];
                }
            }

            System.out.println("#"+test_case);
            for(int i = 0; i < N; i++){
                for(int j = 0; j < 3; j++){
                    System.out.print(res[i][j]+" ");
                }
                System.out.println();
            }
        }
    }
}