import java.util.*;
import java.io.FileInputStream;

class Solution
{
    public static void main(String args[]) throws Exception
    {
        //System.setIn(new FileInputStream("res/input.txt"));

        Scanner sc = new Scanner(System.in);
        int T, row, col, box;
        T=sc.nextInt();

        int[][] puzzle = new int[9][9];
        for(int test_case = 1; test_case <= T; test_case++){

            for(int i = 0; i < 9; i++){
                for(int j = 0; j < 9; j++){
                    puzzle[i][j] = sc.nextInt();
                }
            }

            int i;
            for(i = 0; i < 9; i++){
                row=0; col=0; box=0;
                for(int j = 0; j < 9; j++){
                    row += puzzle[i][j];
                    col += puzzle[j][i];
                    box += puzzle[(i/3)*3 + j/3][(i%3)*3 + j%3];
                }
                if(row!=45 || col!=45 || box!=45)
                    break;
            }
            System.out.println("#"+test_case+" "+(i==9 ? 1:0));
        }
    }
}