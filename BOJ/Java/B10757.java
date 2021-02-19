import java.util.Scanner;
import java.math.BigInteger;

class B10757{
    public static void main(String[] args){
        Scanner scan=new Scanner(System.in); 
        String n=scan.nextLine(); 
        String arr[]=n.split(" "); 
        BigInteger A=new BigInteger(arr[0]); 
        BigInteger B=new BigInteger(arr[1]); 
        
        System.out.println(A.add(B));
    }
}