import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String first_line = bf.readLine();
        String[] n_x = first_line.split(" ");
        int n = Integer.parseInt(n_x[0]); // 문자열을 입력받음
        int x = Integer.parseInt(n_x[1]);
        
        String second_line = bf.readLine();
        String[] test = second_line.split(" ");
        for(int i = 0; i<n; i++){
            int var = Integer.parseInt(test[i]);
            if(var < x){
                System.out.printf("%d ",var);
            }
        }
        bf.close();
    }
}