package lesson001;

public class Examples_dec {

	public static void main(String[] args) {
		// for 루프 _ 구구단생성
		
		int num = 5;
		for(int i = 1; i <= 10; ++i)
		{
			System.out.printf( "%d * %d = %d \n", num, i, num * i );
		}
		
		//for _ 대문자 표시
		
		char c;

	    for(c = 'A'; c <= 'Z'; ++c)
	      System.out.print(c + " ");
		
	}//main
	
}//class
