import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int[] number = new int[9];
        int max = 0;
        int memo = 0;
        for(int i=0; i< 9;i++){
            String n = bf.readLine();
            number[i] = Integer.parseInt(n);
            if(number[i] > max){
                max = number[i];
                memo = i+1;
            }
        }
        System.out.println(max);
        System.out.println(memo);

        bf.close();
    }
}