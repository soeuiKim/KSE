package learning;

public class practice5 {

	public static void main(String[] args) {
		// 피라미드
		int a = 5, b = 0;
		
		   // i는1이고 i 가 a보다 작거나 같을때까지, i는 1씩 커지고, b는 0
		for(int i = 1; i <= a; ++i, b = 0) {
			// c는1 a-i 보다 작거나같을때 까지 c는1씩 커지며
			for(int c = 1; c <= a -i; ++c) {
				System.out.print(" "); //빈 공간 출력
			}
			// 2 곱하기 i -1 값이 b랑 같지 않을때 *출력 후에 b 1증가
			while (b != 2 * i -1) {
				System.out.print("*");
				++b;
			}
			System.out.println();
		}
		
		

	}//main

}//class
