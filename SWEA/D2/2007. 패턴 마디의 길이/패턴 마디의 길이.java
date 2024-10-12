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
        sc.nextLine();

        String word; String words;
        for(int test_case = 1; test_case <= T; test_case++)
        {
            words = sc.nextLine();

            word = words.substring(0, 1);
            for(int i = 1; i < words.length()-1; i++){
                if(word.equals(words.substring(i, i+word.length()))) {
                    break;
                }
                word += words.substring(i, i+1);
            }

            System.out.println("#" + test_case + " " + word.length());
        }
    }
}