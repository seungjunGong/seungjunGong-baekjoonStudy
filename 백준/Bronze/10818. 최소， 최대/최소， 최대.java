import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        String n = bf.readLine();
        int end = Integer.parseInt(n); 
        String list = bf.readLine();
        String[] array = list.split(" ");
        int[] arr_int = new int[end];
        int max = -1000000;
        int min = 1000000;
        for(int i=0; i< end;i++){
            arr_int[i] = Integer.parseInt(array[i]);
            if(max < arr_int[i]){
                max = arr_int[i];
            }
            if(min > arr_int[i]){
                min = arr_int[i];
            }
        }
        System.out.printf("%d %d",min ,max);
        
        bf.close();
    }
}