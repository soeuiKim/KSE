package lesson003;

import java.io.IOException;

public class SysteminTest2 {

	public static void main(String[] args) {
		System.out.println("단어입력후 엔터");
		
		int i;
		
		try {
			while((i= System.in.read()) != '\n') {
				System.out.print((char) i);
			}
			System.out.println();
		} catch (IOException e) {
			System.out.println("입력오류");
			e.printStackTrace();
		}
		
		System.out.println("끝");
		System.exit(0);		
				
				
	}//main

}//class
