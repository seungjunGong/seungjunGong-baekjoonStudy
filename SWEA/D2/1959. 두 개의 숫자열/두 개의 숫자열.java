import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N, M, res=0;
        T=sc.nextInt();

        int K; int[] ki;
        for(int test_case = 1; test_case <= T; test_case++){
            N=sc.nextInt(); M=sc.nextInt();

            int[] ai = new int[N]; int[] bj = new int[M];
            for(int i = 0; i < N; i++) ai[i] = sc.nextInt();
            for(int j = 0; j < M; j++) bj[j] = sc.nextInt();

            if(N > M){
                K=N; N=M; M=K;
                ki=ai; ai=bj; bj=ki;
            }

            int sum;
            for(int j = 0; j <= M-N; j++){
                sum=0;
                for(int i = 0; i < N; i++){
                    sum += bj[j+i]*ai[i];
                }
                if(j==0) res=sum;
                res = Math.max(sum, res);
            }

            System.out.println("#"+test_case+" "+res);

        }
    }
}