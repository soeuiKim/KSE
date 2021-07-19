package lesson001;

public class E010_forStmt {

	public static void main(String[] args) {
		//for (initialExpression; testExpression; updateExpression) 
	    //    (       초기식,       조건(종결)식,    증감식	      )
		
	int n = 5;
		// for Loop
	for (int i = 1; i <= n; ++i) {
		System.out.println("Java is fun");
	}
		System.out.println("프로그램종료");
	
	System.out.println("============================");
	
	 int sum = 0;
	    int m = 1000;
	    
	    //for loop ( 초기식 i=1, 테스트식 i <= n;를 1씩 증가하며)
	    for (int i = 1; i <= m; ++i) {
	     
	      sum += i;     // sum = sum + i
	    }//for sum
	       
	    System.out.println("Sum = " + sum);
	 

	    
	    
	    
	}//main
}//class
	