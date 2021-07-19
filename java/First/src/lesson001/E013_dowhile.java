package lesson001;

public class E013_dowhile {

	public static void main(String[] args) {
		// do while
		
		int i = 1;
		
		do {
			System.out.println(i);
			i++;
		} while (i <10);

		
		
		i = 1 ;
		while(i <= 10) {
			System.out.println(i);
			i++;
		}  // ;가 없다 _ do while 구문과 형태적으로 다름을 인지하고있어야함.
		
	}//main

}//class
