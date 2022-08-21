import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); // 문자열을 입력받음
        
        int[] sum = new int[n];
        int[] a = new int[n];
        int[] b = new int[n];
        for(int i = 0; i<n;i++){
            String test = bf.readLine();
            String[] multiply = test.split(" ");
            a[i] = Integer.parseInt(multiply[0]);      
            b[i] = Integer.parseInt(multiply[1]);
            sum[i] = a[i] + b[i];
        }
        for(int i = 0; i<n; i++){
           System.out.printf("Case #%d: %d + %d = %d\n", i+1, a[i], b[i], sum[i]);
        }
        bf.close();
    }
}