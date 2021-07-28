package lesson003;

import java.io.IOException;

public class SysteminTest1 {

	public static void main(String[] args) {
		int i;
		
		//입력받기
	
		try {
			System.out.println("문자입력");
			i = System.in.read();
			System.out.println(i);
			System.out.println((char)(i-32));
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
			System.out.println("입력 오류 발생");
		}
		
		System.out.println("프로그램종료..빠잉");
		
		
	}//main

}//class
