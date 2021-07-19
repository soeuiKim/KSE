package lesson001;

import java.util.Scanner;

public class E005_inputoutput {

	public static void main(String[] args) {
		
		//자바의 출력문
		//System.out.println(); or
	    //System.out.print(); or
    	//System.out.printf();
		
		System.out.println("Hello java"); //행단위 출력
		System.out.println("Hello java"); //행단위 출력
		
		System.out.print("print\n"); 
		System.out.print("print\n"); 
		
		System.out.printf("%d\n",10);
		System.out.printf("값 %d\n",10);
		
		System.out.println("Hello"+"Java"); //concatenated(두개문자를 결합)
		
		//===============input Statement
		// create an object of Scanner
		//클래스이름(타입) 객체참조변수 = new 클래스생성자
		Scanner input = new Scanner(System.in);

		// take input from the user 사용자로부터 입력을 받는것.
		System.out.println("정수형 데이터를 입력해주세요.");
		int number = input.nextInt();
		System.out.printf("숫자 : %d\n",number);

		input.nextLine(); //개행문자 제거용_엔터입력시 넘어가는현상방지
		
		System.out.println("이름을 입력해주세요.");
		String name = input.nextLine();
		
		System.out.printf("숫자 : %d, 이름: %s\n",number, name);
		
		input.close(); // resource_리소스반납(메모리공간확보를위해서)
		
		
		
		
		
	}
}
