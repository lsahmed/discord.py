import java.util.Scanner;
import java.util.Random;
public class _temp{
    public static void main(String args[]){
        String pass = "abcdefghijklmnopqrstuvwxyz";
        Random random = new Random();
        int rand = random.nextInt();
        System.out.println(pass.charAt(rand));
    }
}