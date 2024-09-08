import java.util.*;
public class _temp{
    public static void main(String args[]){
        Random random = new Random(); // Random class to generate random numbers.
        Scanner sc = new Scanner(System.in); // Scanner class to take inputs
        
        int nums[] = new int[10];
        for(int i=0; i<10; i++){
            nums[i] = i;
        }
        int num = random.nextInt(0,nums.length);
        System.out.println(num);
        for(int i=num;i>-1;i--){
            System.out.print(nums[i]);
        }
        System.out.println();
        
    }
}