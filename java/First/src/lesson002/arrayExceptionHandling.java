package lesson002;

public class arrayExceptionHandling {

	public static void main(String[] args) {
		// try catch 구문을 이용한 예외처리_파일핸들링,디비검색처리,질의처리 등
		
		int[] arr = new int[5];
		
		try {
			for(int i = 0; i <= 5 ; i++) {
			arr[i] = i;
			System.out.println(arr[i]);
			}
		} catch (ArrayIndexOutOfBoundsException e) {
			System.out.println("인덱스가 범위를 벗어났습니다.");
			e.printStackTrace();
		}//end of catch (Exception e)
		
		
		
		
		System.out.println("프로그램 종료");
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	}//main

}//class
