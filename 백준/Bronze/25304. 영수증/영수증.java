import java.util.Scanner;

public class Main {
    public static void main(String[] args){
        Scanner scan = new Scanner(System.in);
        int sum = scan.nextInt();
        int n = scan.nextInt();
        scan.nextLine();
        int runningtotal = 0;
        String[] n_line = new String[n];
        for(int i = 0; i<n;i++){
            n_line[i] = scan.nextLine();
            String[] multiply = n_line[i].split(" ");
            int a = Integer.parseInt(multiply[0]);      
            int b = Integer.parseInt(multiply[1]);
            runningtotal += (a*b);
        }
        if(runningtotal == sum){
            System.out.println("Yes");
        }
        else{
            System.out.println("No");
        }
        scan.close();
    }
}