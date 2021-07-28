package lesson003;

import java.io.FileInputStream;
import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class FileReaderTest1 {

	public static void main(String[] args) {
		try (FileReader fr = new FileReader("C:/Users/user12/Desktop/input2.txt")) {
		
		int i;

		while((i = fr.read()) != -1) {
			System.out.print((char)i);			
		}
		System.out.println("\n읽기완료");


		} catch (FileNotFoundException fe) {

			System.out.println("지정파일 찾을수 없음");
					fe.printStackTrace();

		} catch (IOException e) {

			System.out.println("파일 입력 처리 오류");
			e.printStackTrace();  //습관적으롱!

		}

		System.out.println("프로그램 정상종료");

	}

}
