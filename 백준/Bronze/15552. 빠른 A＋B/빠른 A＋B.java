import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.IOException;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); // 문자열을 입력받음
        BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
        
        int[] sum = new int[n];
        for(int i = 0; i<n;i++){
            String test = bf.readLine();
            String[] multiply = test.split(" ");
            int a = Integer.parseInt(multiply[0]);      
            int b = Integer.parseInt(multiply[1]);
            sum[i] = (a + b);
        }
        for(int i = 0; i<n; i++){
            bw.write(sum[i]+"\n");
        }
        bf.close();
        bw.close();
    }
}