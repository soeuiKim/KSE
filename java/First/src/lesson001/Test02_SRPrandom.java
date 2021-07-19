package lesson001;

import java.util.Scanner;

public class Test02_SRPrandom {
	
	public static void main(String[] args) {
		
		// if 문 활용 연습 - 가위 바위 보 게임
		int com = (int) Math.random() * 10 % 3 + 1;
		int human;
		String winner = "";
		String cp = "", hp="";
		Scanner input = new Scanner(System.in);
		System.out.println("가위(1), 바위(2), 보(3) 중 하나 선택하세요.");
		human = input.nextInt();
		
		if(com == 1) {// 컴이 가위를 내었다면
			cp = "가위";
			if(human == 1) { // 사람이 가위를 내었을 때
				winner = "both";
				hp = "가위";
			}else if(human == 2) {// 사람이 바위를 내었을 때
				winner = "human";
				hp = "바위";
			}else {//사람이 보를 내었을 때
				winner = "computer";
				hp = "보";
			}
		}else if (com == 2) { // 컴이 바위를 내었다면
			cp = "바위";
			if(human == 1) { // 사람이 가위를 내었을 때
				winner = "computer";
				hp = "가위";
			}else if(human == 2) {// 사람이 바위를 내었을 때
				winner = "both";
				hp = "바위";
			}else {//사람이 보를 내었을 때
				winner = "human";
				hp = "보";
			}
		}else { // 컴이 보를 내었다면
			cp = "보";
			if(human == 1) { // 사람이 가위를 내었을 때
				winner = "human";
				hp = "가위";
			}else if(human == 2) {// 사람이 바위를 내었을 때
				winner = "computer";
				hp = "바위";
			}else {//사람이 보를 내었을 때
				winner = "both";
				hp = "보";
			}
		}
		
		System.out.printf("%s(이)가 이겼어요. 컴: %s, 너님: %s", winner, cp, hp);
		
		
		
	}//main

}//class
