package lesson001;

public class E012_forStmt {

	public static void main(String[] args) {
		// for each statement
		
			
		 // create an array
		 int[] numbers = {3, 7, 5, -5};  //여러개의 데이터들이 모인것collections
		    
		 // iterating through the array 
		 for (int number: numbers) {
		       System.out.println(number);
		 }// for number

	System.out.println("============================");   
		    
		int[] a = {1,2,3,4,5};
		
		for(int number : a) {
			System.out.println(number);
		}
		
//		String str = "korea";
//		for(char ch : str) {
//		System.out.println(ch);
//		}
		
		
		 // Infinite for Loop

		for (int i = 1; i <= 10; --i) {
			System.out.println("Hello");
		}  // = for(;;){sysout ".."}
		
		
		
	}//main

}//class
