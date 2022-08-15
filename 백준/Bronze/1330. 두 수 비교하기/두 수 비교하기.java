import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String input = scan.nextLine();
        String[] num = input.split(" ");
        int a = Integer.parseInt(num[0]);
        int b = Integer.parseInt(num[1]);
    
        if(a>b){
            System.out.println(">");
        }
        else if(a<b){
            System.out.println("<");
        }
        else {System.out.println("==");}
        scan.close();
    }
}
