import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, fHour, fMin, bHour, bMin, h, m;

        T=sc.nextInt();
        for(int test_case = 1; test_case <= T; test_case++){
            fHour = sc.nextInt(); fMin = sc.nextInt();
            bHour = sc.nextInt(); bMin = sc.nextInt();
            h = (fMin + bMin) / 60;
            m = (fMin + bMin) % 60;

            h = h+fHour+bHour;
            if(h > 12) h = h - 12;

            System.out.println("#"+test_case+" "+h+" "+m);
        }
    }
}