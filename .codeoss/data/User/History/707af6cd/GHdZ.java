import java.util.*;
public class _temp{
    public static void main(String args[]){
        Random random = new Random(); // Random class to generate random numbers.
        Scanner sc = new Scanner(System.in); // Scanner class to take inputs
        
        int nums[] = new int[10];
        for(int i=0; i<10; i++){
            nums[i] = i;
        }
        int num = random.nextint(0,12);
        for(num;num>0;num--){
            System.out.print(nums[num]);
        }
        
    }
}