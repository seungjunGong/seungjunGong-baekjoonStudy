import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        int year = scanner.nextInt();
        year -= 543;
        System.out.println(year);
        scanner.close();
    }
}