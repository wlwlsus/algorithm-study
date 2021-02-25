import java.util.Scanner;
import java.math.BigInteger;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String n = sc.nextLine();
        String arr[] = n.split(" ");
        BigInteger A = new BigInteger(arr[0]);
        BigInteger B = new BigInteger(arr[1]);

        System.out.println(A.add(B));
        sc.close();
    }
}