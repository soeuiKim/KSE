package lesson001;

import java.util.Scanner;

public class Test01_SRP {

	public static void main(String[] args) {
		
		int srp = 1;
		
		if (srp < 2) { 
			System.out.println("Rack");
		}else if (srp > 2){
			System.out.println("Scissor");
		}else {
			System.out.println("Paper");
		}
		
		System.out.println("you win");
		
		
		System.out.println("===========================");
		
		
		Scanner input = new Scanner(System.in);

		System.out.println("가위(1), 바위(2), 보(3)를 입력해 주세염");
		int number = input.nextInt();
		System.out.printf("내가 낸것 %d\n",number);
		
		input.close(); 
		
		
		
		switch( number ) {
		case 1:
			System.out.println(" 상대방이 보(3)를 냈습니다.");
			break; 
		case 2:
			System.out.println(" 상대방이 가위(1)를 냈습니다. ");
			break;
		case 3:
			System.out.println(" 상대방이 바위(2)를 냈습니다.");
			break;
		default:
			System.out.println("다시 선택해 주세요.");
			break;
	}//switch
		
		System.out.println("무조건 이겼습니당");
		

	}//main

}//class
