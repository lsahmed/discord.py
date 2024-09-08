import java.util.Scanner;
import java.util.Random;
public class _temp{
    public static void main(String args[]){
        String pass = "1234567890acdefghijklmnopqrstuvwyzABCDEFGHIJKLMOPQRSTUVWXYZb!@#$%^&*()_+:";
        
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter length of your password: ");
        int lenPass = sc.nextInt();

        for(int i=0; i<=lenPass;i++){
            Random random = new Random();
            int rand = random.nextInt(0,pass.length());
            
            
            
        }
        System.out.println();
    }
}