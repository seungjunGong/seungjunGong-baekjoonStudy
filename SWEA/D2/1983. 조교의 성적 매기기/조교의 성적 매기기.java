import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, N, K, a, b, c;

        T=sc.nextInt();
        String[] score =
                new String[]{"A+", "A0", "A-",
                        "B+", "B0", "B-",
                        "C+", "C0", "C-", "D0"};
        for(int test_case = 1; test_case <= T; test_case++){
            N=sc.nextInt(); K=sc.nextInt();

            List<List<Integer>> totalList = new ArrayList<>();
            for(int i = 1; i <= N; i++)
            {
                a=sc.nextInt(); b=sc.nextInt(); c=sc.nextInt();
                totalList.add(Arrays.asList(a*35 + b*45 + c*20, i));
            }
            totalList.sort(Comparator.comparing(
                    (List<Integer> o)->o.get(0)).reversed()
            );

            for(int i = 0; i < N; i++){
                if(totalList.get(i).get(1) == K)
                    System.out.println("#" + test_case + " " + score[i/(N/10)]);
            }
        }
    }
}