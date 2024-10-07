import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T;
        T=sc.nextInt();
        sc.nextLine(); // 숫자를 읽은 후에 빈 줄을 처리

        String line, year, month, day;
        int[] days = {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int m, d;

        for(int test_case = 1; test_case <= T; test_case++)
        {
            line = sc.nextLine();

            year = line.substring(0, 4);
            month = line.substring(4, 6);
            day = line.substring(6, 8);

            m = Integer.parseInt(month);
            d = Integer.parseInt(day);

            if(d > 0 && days[m] >= d){
                System.out.printf("#%d %s/%s/%s\n", test_case, year, month, day);
            }else { System.out.println("#" + test_case + " -1"); }
        }

    }
}