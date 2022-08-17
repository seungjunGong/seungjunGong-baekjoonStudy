import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int count = scan.nextInt();
        scan.nextLine();
        String[] test = new String[count];
        int[] test_print = new int[count]; 

        for(int i = 0; i<count;i++){
            test[i] = scan.nextLine();
            String[] add = test[i].split(" ");
            int a = Integer.parseInt(add[0]);
            int b = Integer.parseInt(add[1]);
            test_print[i] = a+b;
        }
        for(int i = 0; i<count;i++){
            System.out.println(test_print[i]);
        }
        scan.close();
    }
}