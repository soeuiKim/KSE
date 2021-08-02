package learning;

public class practice4 {

	public static void main(String[] args) {
		// 짝수 구구단
		int t;
		int n;
		
//		for(t=2;t<=9;t++) {
//			if(t%2 != 0) continue;
//			for(n=1;n<=9;n++) {
//				System.out.println(t + "X" + n + "=" + t * n);
//			}//inner for
//			System.out.println();
//		}//side for
		
		// 구구단 단보다 곱하는수가 작거나 같은경우만
		
		for(t=2;t<=9;t++) {
			for(n=1;n<=9;n++) {
				if( t < n ) break;
				System.out.println( t + "X" + n + '=' + t * n);
			}
			System.out.println();
		}
		
		
		
		
		
		
		
		
	}//main

}//class
