package learning;

public class practice2 {

	public static void main(String[] args) {
		// 성적따라 학점부여 if...else if
		
		int S = 99;
		char G ;
		
		if (S >= 90) {
			G = 'A';
		}
		else if(S >= 80) {
			G = 'B';
		}
		else if(S >= 70) {
			G = 'C';
		}
		else if(S >= 60) {
			G = 'D';
		}
		else { 
			G = 'F';
		}
		System.out.println("성적은"+ G +"입니다");
		
		//switch case
		
		int e = 3;
		
		switch (e) {
		
			case 1 : System.out.println("1층 약국"); break;
			case 2 : System.out.println("2층 정형외과"); break;
			case 3 : System.out.println("3층 피부과"); break;
			case 4 : System.out.println("4층 치과"); break;
			default : System.out.println("5층 헬스클럽"); break;
		}// switch e
		
		System.out.println();
		
		// 구구단 NestedLoop
		
		int r;
		int t;
		
		for(r =2; r <= 9; r++) {
			for(t =1; t <=9; t++) {
				System.out.println(r + "X" + t + "=" + r * t);
			}//inner for
			System.out.println(); // 한줄띄우기
		}//side for
		
		
		
		
		
	}//main

}//class
