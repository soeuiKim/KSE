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
		
	    
	    
	    //for 루프_소문자나열
	    
	    char s;
	    
	    for(s = 'a'; s <= 'z'; ++c)
	    	System.out.print(c + " ");
	    
	    
	    //윤년확인
	    
	    int year = 1996;
	    boolean leap = false;
	    
	    if (year % 4 == 0) {
	      
	      if (year % 100 == 0) {
	       
	        if (year % 400 == 0)
	          leap = true;
	        else
	          leap = false;
	      }
	      else
	        leap = true;
	    }
	    else
	      leap = false;

	    if (leap)
	      System.out.println(year + " is a leap year.");
	    else
	      System.out.println(year + " is not a leap year.");
	    
	}//main
	
}//class
