package lesson001;

import java.util.Scanner;

public class Examples_dec4 {

	public static void main(String[] args) {
		// 단어를 입력받아 사전순으로 출력

		Scanner input = new Scanner(System.in);

		System.out.println("단어를 입력해주세요.(여러단어를 ',' 사용하여 입력)");
		String[] words = {"","", "", "",""};
		
		for(int i = 0;i>=0;i++ ) {
			words[i] = input.nextLine();
			if(words[i] == "end") break;
		}

		System.out.println(words);

		for (int a = 0; a < words.length - 1 ; ++a) { 
			for (int b = a + 1; b< words.length ; ++b) {
				if (words[a].compareTo(words[b]) > 0) { 
					String temp = words[a]; 
					words[a] = words[b]; 
					words[b] = temp; 
				} // if } 
			}// for2 
		}// for1

		System.out.println("사전순:");

		System.out.print(words);


	}// main

}// class
