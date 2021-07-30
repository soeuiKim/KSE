package lesson003;

import java.util.Scanner;

public class LeapYear {

	public static void main(String[] args) {
		// 김소의
		
		Scanner input = new Scanner(System.in);
		
		System.out.println(" 연도를 입력해주세요 ");
		
		int y = input.nextInt();
		
	    boolean leap = false;

	    if ( y % 4 == 0) {

	      if ( y % 100 == 0) {

	        if ( y % 400 == 0)
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
	      System.out.println( y + "년은 윤년입니다 ");
	    else
	      System.out.println( y + "년은 윤년이 아닙니다 ");
		

	}

}
