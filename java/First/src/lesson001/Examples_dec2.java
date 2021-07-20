package lesson001;

import java.util.Scanner;

public class Examples_dec2 {

	public static void main(String[] args) {
		//switch case 계산기

		
		  char operator; Double number1, number2, result;
		  
		  Scanner input = new Scanner(System.in);
		  
		  System.out.println("숫자를 입력해 주세요"); number1 = input.nextDouble();
		  
		  System.out.println("연산자를 선택해주세요 : +, -, *, /"); operator =
		  input.next().charAt(0);
		  
		  System.out.println("숫자를 입력해 주세요"); number2 = input.nextDouble();
		  
		  switch (operator) {
		  
		  case '+': result = number1 + number2; System.out.println(number1 + " + " +
		  number2 + " = " + result); break;
		  
		  case '-': result = number1 - number2; System.out.println(number1 + " - " +
		  number2 + " = " + result); break;
		  
		  case '*': result = number1 * number2; System.out.println(number1 + " * " +
		  number2 + " = " + result); break;
		  
		  case '/': result = number1 / number2; System.out.println(number1 + " / " +
		  number2 + " = " + result); break;
		  
		  default: System.out.println("정확히 입력해주세요"); break; }
		  
		  input.close();
		 
	    
	    //피라미드
	    
	    int rows = 5, k = 0;
	    
	    // i=1로 시작,i가 rows보다 작거나 같을때까지 i는 1씩 증가, k는 0
	    for(int i =1; i <= rows; ++i, k=0 ) {
	    	
	    	//space 1, s가 r-i 보다 작거나 같을때까지 s 1씩 증가
	    	for(int space = 1; space <= rows -i; ++space) {
	    		
	    		System.out.print(" ");
	    	}//for space
	    	
	        while (k !=2*i-1) {
	    		System.out.print("*");
	    		++k;
	    	}//while
	    	
	    	System.out.println();
 	    }//for i
		
	    
	    
	    //while,if사용하여 LCM(최소공배수)
	    int n1 = 75, n2 = 150, lcm;

	    // n1과 n2의 최대수는 lcm에 저장 
	    lcm = (n1 > n2) ? n1 : n2;

	    while(true) {
	    	// lcm를 n1으로 나누고 남은 몫이 0일때 &&(and)와
	    	// lcm을 n2로 나누고 남은 몫이 0일때
	      if( lcm % n1 == 0 && lcm % n2 == 0 ) {
	        System.out.printf("%d 와 %d 의 LCM(최소공배수)는? %d ", n1, n2, lcm);
	        break;
	        
	      }//if
	      
	      ++lcm;
	      
	    }//while
	    
	}//main

}//class
