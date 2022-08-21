import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(bf.readLine()); // 문자열을 입력받음
        
        for(int i = 1; i<=n; i++){
            for(int k = 1; k<=i; k++){
                System.out.printf("*");
            }
            System.out.println();
        }
        bf.close();
    }
}