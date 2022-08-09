import java.util.*;

public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String num = scanner.nextLine();
        String[] number = num.split(" ");
        int a = Integer.parseInt(number[0]);
        int b = Integer.parseInt(number[1]);
        int c = Integer.parseInt(number[2]);

        System.out.println((a+b)%c);
        System.out.println(((a%c)+(b%c))%c);
        System.out.println((a*b)%c);
        System.out.println(((a%c)*(b%c))%c);
        scanner.close();       
    }
}
