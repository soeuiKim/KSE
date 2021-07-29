package learning;

import java.util.Scanner;

public class practice3 {

	public static void main(String[] args) {
		// 사칙연산
		Scanner in = new Scanner(System.in);
		
		System.out.println("숫자입력");
		
		int n;
		n = in.nextInt();
		
		System.out.println("연산자(+,-,*,/)입력");
		char o;
		o = in.next().charAt(0);
		
		System.out.println("숫자입력");
		int u ;
		u = in.nextInt();
		
//	 switch case문
		int re;
		switch (o) {
			case '+' : re = n + u; 
			 	System.out.println("답  "+re);
			 	break;
			case '-' : re = n - u;
				System.out.println("답  "+re);
				break;
			case '*' : re = n * u; 
			 	System.out.println("답  "+re);
				break;
			case '/' : re = n / u; 
				System.out.println("답  "+re);
				break;
			default : System.out.println("잘못입력했음"); break;
		}//switch
		
		in.close();
		
		

//   if..else if문		
//		int r = 0;
//		
//		if (o == '+') {
//			r = n + u;
//		}
//		else if (o == '-') {
//			r = n - u;
//		}
//		else if (o == '*') {
//			r = n * u;
//		}
//		else if (o == '/') {
//			r = n / u;
//		}
//		else {
//			System.out.println("잘못입력했음");
//			return;
//		}
//		System.out.println(r + "입니다");
		
		
		

	}//main

}//class
