import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        String alps;
        alps=sc.nextLine();

        for(int i = 0; i < alps.length(); i++){
            System.out.print((int)alps.charAt(i) - 64 + " ");
        }

    }
}