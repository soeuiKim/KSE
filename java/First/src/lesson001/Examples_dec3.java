package lesson001;

import java.util.Scanner;

public class Examples_dec3 {

	public static void main(String[] args) {
		// 암스트롱번호_양의 정수를 암스트롱차수 라고 한다.
		// 암스트롱 숫자가 3자리일때 각 숫자의 세제곱합은 숫자 자체와 같음.
		
		Scanner input = new Scanner(System.in);
		System.out.println("숫자를 입력해 주세요.");
		
		int number = input.nextInt(), originalNumber, remainder, result = 0;
		
		
		input.close();
		
		originalNumber = number;
		
		// != 같지않다
		while ( originalNumber != 0)
		{
			remainder = originalNumber % 10;
			result += Math.pow(remainder, 3);
			originalNumber /= 10; // /=는 변수를 나눈후 그 값을 변수에 대입
								 // ex) N /= 2   =  N = N/2
		}
		
		if(result == number)
			System.out.println(number + "암스트롱 번호입니다.");
		else
			System.out.println(number + "암스트롱 번호가 아닙니다.");
		
		
		//
		
		
	}//main

}//class
