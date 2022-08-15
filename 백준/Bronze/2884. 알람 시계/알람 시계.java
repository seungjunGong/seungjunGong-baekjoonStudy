import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String x = scan.nextLine();
        String[] num = x.split(" ");
        int hour = Integer.parseInt(num[0]);
        int minute = Integer.parseInt(num[1]);
        
        minute -= 45;
        if(minute < 0){
            minute = 60 + minute;
            hour -= 1;
            if(hour == -1){
                hour = 23;
            }
        } 
        System.out.printf("%d %d", hour, minute);
        scan.close();
    }
}