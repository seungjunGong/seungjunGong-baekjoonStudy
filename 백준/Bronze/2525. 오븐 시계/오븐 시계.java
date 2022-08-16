import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        String x = scan.nextLine();
        String[] num = x.split(" ");
        int hour = Integer.parseInt(num[0]);
        int minute = Integer.parseInt(num[1]);        
        int time = scan.nextInt();
        
        if(time>=60){
            hour += (int)(time / 60);
            minute += time % 60;
        }
        else{
            minute += time;
        }
        if(minute>59){
            minute -= 60;
            hour += 1;
        }
        if(hour>23){
            hour -= 24;
        }
        System.out.printf("%d %d" ,hour ,minute);
        scan.close();
    }
}