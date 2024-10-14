import java.util.*;
import java.io.FileInputStream;

class Solution
{
    static int N, M;
    static int hit(int x, int y, int[][] area){
        int res = 0;
        for(int i = x; i < x+M; i++) {
            for (int j = y; j < y + M; j++) {
                res += area[i][j];
            }
        }
        return res;
    }
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, maxHit;
        T=sc.nextInt();
        
        for(int test_case = 1; test_case <= T; test_case++)
        {
            N = sc.nextInt(); M = sc.nextInt();
            int[][] area = new int[N][N];
            
            // 파리 초기화
            for(int i = 0; i < N; i++){
                for(int j = 0; j < N; j++){
                    area[i][j] = sc.nextInt();
                }
            }

            maxHit = 0;
            for(int i = 0; i <= N-M; i++){
                for(int j = 0; j <= N-M; j++){
                    maxHit = Math.max(hit(i, j, area), maxHit);
                }
            }
            System.out.println("#" + test_case + " " + maxHit);
        }
    }
}