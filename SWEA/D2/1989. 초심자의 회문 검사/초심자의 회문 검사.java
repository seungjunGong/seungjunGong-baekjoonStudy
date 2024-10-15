import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, len;
        T=sc.nextInt();
        sc.nextLine();

        String word; boolean check;
        for(int test_case = 1; test_case <= T; test_case++)
        {
            word = sc.nextLine();
            len = word.length(); check = false;
            for(int i = 0; i < len/2; i++){
                if(word.charAt(i) != word.charAt(len-1-i)){
                    check = true;
                    break;
                }
            }
            System.out.println("#"+test_case+" "+ (check ? 0 : 1));
        }
    }
}