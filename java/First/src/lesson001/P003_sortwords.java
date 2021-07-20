package lesson001;

import java.util.Scanner;

public class P003_sortwords {

	public static void main(String[] args) {
	
		
		Scanner keyin = new Scanner(System.in);
		System.out.println("단어들을 스페이스로 구분하여 입력해주세요");
		
		String inwords = keyin.nextLine();
		String[] words = inwords.split(" ");
		String temp;
		
		// 정렬작업
		// i번째 단어 기준으로 
		for(int i = 0; i < words.length - 1 ; i++) {
			//i+1번째 단어부터 끝까지 비교
			for(int j = i+1; j < words.length ; j++) {
				
				if(words[i].compareTo(words[j]) > 0) {
					
					temp = words[i];
					words[i] = words[j];
					words[j] = temp ;
					
				}//end of if
			}//inner for loop (for2)
		}//end of outer for loop (for1)
		
		//정렬후 출력
		for(int i = 0 ; i < words.length ; i++) {
			System.out.println(words[i]);
		}
		
	}//end of main

}//end of class
