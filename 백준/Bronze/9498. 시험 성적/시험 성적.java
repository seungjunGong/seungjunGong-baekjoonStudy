import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int num = scan.nextInt();
        if(num<60){
            System.out.println("F");
        }
        else if(num<70){
            System.out.println("D");
        }
        else if(num<80){
            System.out.println("C");
        }
        else if(num<90){
            System.out.println("B");
        }
        else if(num<=100){
            System.out.println("A");
        }
        scan.close();
    }
}