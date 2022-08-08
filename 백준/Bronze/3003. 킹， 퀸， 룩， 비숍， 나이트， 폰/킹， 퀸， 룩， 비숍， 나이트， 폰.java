import java.util.*;
public class Main {
    public static void main(String[] args){
        Scanner scanner = new Scanner(System.in);
        String count = scanner.nextLine();
        int[] black = {1, 1, 2, 2, 2, 8};
        String[] white = count.split(" ");
        int[] cal = new int[6];
        for(int i = 0; i<6; i++){
            cal[i] = Integer.parseInt(white[i]);
            cal[i] = black[i] - cal[i];
            System.out.print(cal[i] + " ");
        }
        scanner.close();
    }
}