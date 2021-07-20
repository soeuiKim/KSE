package lesson001;

public class E015_array2d {

	public static void main(String[] args) {
		// declare array 배열 선연
		
		int[] arry1d;
		int[][] arry2d;
		
		arry1d = new int[] {1,2,3}; //선언된 배열에 값 초기화
		arry2d = new int[][] {
								{1,2},
								{4,5,6},
								{7,8,9}
							 };
		//개별 요소에 접근 index 사용
			System.out.println("1차원 배열 arry1d의 값");
			for(int i = 0; i < arry1d.length ; i++) {
				System.out.printf("%3d   ",arry1d[i]);
			}
			System.out.println(); // 줄바꿈용
			
			// 2차원 배열 요소에 대한 접근
			// nested for loop 사용
			
			System.out.println("2차원 배열 arry2d의 값");
			
			for(int row = 0; row < arry2d.length; row++) {
				for(int col = 0; col < arry2d[row].length; col++) {
					System.out.printf("%3d ", arry2d[row][col]);
				}//end of inner for loop
			}//end of outer for loop
			
			System.out.println(); // 줄바꿈용

	}//main

}//class
