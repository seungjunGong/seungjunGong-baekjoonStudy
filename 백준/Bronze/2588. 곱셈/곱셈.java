import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int num1 = scanner.nextInt();
        int num2 = scanner.nextInt();
        int lastnum = num2 % 10;
        int secondnum = (int)(((num2 % 100) - lastnum)/10);
        int firstnum = (int)((num2 - (num2 % 100))/100);

        System.out.println(num1 * lastnum);
        System.out.println(num1 * secondnum);
        System.out.println(num1 * firstnum);
        System.out.println(num1 * num2);
        scanner.close();       
    }
}
