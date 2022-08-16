import java.util.Scanner;
import java.util.Arrays;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String x = scan.nextLine();
        String[] num = x.split(" ");
        int[] sort_num = new int[num.length];
        for(int i = 0; i<num.length;i++){
            sort_num[i] = Integer.parseInt(num[i]);
        } 
        Arrays.sort(sort_num);
        int a = sort_num[2];
        int b = sort_num[1];
        int c = sort_num[0];

        if(a == c){
            System.out.println(10000+(b*1000));
        }
        else if(b == a || b == c){
            System.out.println(1000+(b*100));
        }
        else{
            System.out.println(a*100);
        }
        scan.close();
    }
}