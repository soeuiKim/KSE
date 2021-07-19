package lesson001;

public class E008_IfelseifStmt {

	public static void main(String[] args) {
		// if...else...if statement
		// 세개 이상의 선택을 비교해야할 때

		int score = 75;
		
		if(score >= 90) {
			System.out.println("A");
		}else if (score >= 80) {
			System.out.println("B");
		}else if (score >= 70) {
			System.out.println("C");
		}else if (score >= 60) {
			System.out.println("D");
		}else {
			System.out.println("F");
		}
		
		System.out.println("프로그램종료");
		
		System.out.println("============");
		 int number = 10;

		    // checks if number is greater than 0
		    if (number > 0) {
		      System.out.println("The number is positive.");
		    }
		    
		    // 다른 실행문 입력 x _ 실행문이 들어가면 else가 if를 잃어버림
		    // execute this block
		    // if number is not greater than 0
		    
		    else {
		      System.out.println("The number is not positive.");
		    }

		    System.out.println("Statement outside if...else block");
		
	}//main

}//class
