package DEU;

import java.util.Arrays;
import java.util.Scanner;

public class X5545x1 {
    public static void main(String[] args) {
		Scanner scan = new Scanner(System.in);
		
		int N = scan.nextInt();			// 토핑의 종류 수
		int dow = scan.nextInt();		// 도우 가격
		int toping = scan.nextInt();	// 토핑 가격
		int dowCal = scan.nextInt();	// 도우의 열량
		int[] topingCal = new int[N];
		int index = topingCal.length - 1;	// 토핑 칼로리가 가장 높은 요소 부터 비교
		for(int i=0; i<topingCal.length; i++) 	// 토핑의 열량
			topingCal[i] = scan.nextInt();
		
		int beforePerCal = dowCal / dow;	// 이전 1원당 칼로리
		int afterPerCal = dowCal;	// 이후 1원당 칼로리
		int totalCal = dowCal;			// 토핑 올린 후 총 칼로리
		int price = dow;			// 가격

		// 토핑의 열량 정렬 => 가장 마지막 요소 - 열량이 가장 높음.
		Arrays.sort(topingCal);
		
		while(true) {
			// 토핑 한개 추가한 뒤 1원당 칼로리
			// (200 + 300) / (12 + 2) ... (200 + 300 + 100) / (12 + 2 + 2)
			price += toping;
			totalCal += topingCal[index--];
			afterPerCal = totalCal / price; 
			if(beforePerCal > afterPerCal)
				break;
			else {
				beforePerCal = afterPerCal;
			}
		}
		
		System.out.println(beforePerCal);
		scan.close();
	}
}
