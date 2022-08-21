import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int end = 1;
        int[] sum = new int[10000];
        for(int i=0; i<end; i++){
            String line = bf.readLine();
            String[] a_b = line.split(" ");
            int a = Integer.parseInt(a_b[0]);
            int b = Integer.parseInt(a_b[1]);
            sum[i] = a+b;
            if(a==0 || b==0){
                end--;
            }
            end++;
        }
        for(int i=0;i<end-1;i++){
            System.out.println(sum[i]);
        }
        bf.close();
    }
}