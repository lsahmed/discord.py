import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your input: ");
        int n = sc.nextInt();

        for(int i=1;i<=n;i++){
            for(j=1;j<=n-i;j++){
                System.out.print(" ");
            }
            int odi = (2*i)-1;
            for(int j=1;j<=odi;j++){
                System.out.print("*");
            }
            System.out.println();
        }
     }

    }


