package lesson003;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.IOException;

public class FileinputStreamTest1 {

	//바탕화면에 txt파일생성 후
	public static void main(String[] args) {
		try(FileInputStream fis = new FileInputStream("C:/Users/user12/Desktop/tinput.txt")){ 
			int i;
			while ( (i = fis.read()) != -1){
				System.out.println((char)i);
			}
			System.out.println("끝");
		} catch (FileNotFoundException e) {
			e.printStackTrace();
		} catch (IOException e) {
			e.printStackTrace();
		}
		
		
//		int i;
//		
//		while((i = fis.read()) != -1) {
//			System.out.println((char)i);			
//		}
//		System.out.println("읽기완료");
//		
//		try {                         // 경로지정
//			fis = new FileInputStream("C:/Users/user12/Desktop/tinput.txt");
//			
//			System.out.println(fis.read());
//			System.out.println(fis.read());
//			System.out.println(fis.read());
//			
//		} catch (FileNotFoundException fe) {
//			
//			System.out.println("지정파일 찾을수 없음");
//			fe.printStackTrace();
//			
//		} catch (IOException e) {
//			
//			System.out.println("파일 입력 처리 오류");
//			e.printStackTrace();  //습관적으롱!
//			
//		}
//		
//		System.out.println("프로그램 정상종료");
		

	}//main

}//class
