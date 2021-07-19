package lesson001;

public class E009_SwitchCase {

	public static void main(String[] args) {
		//jopnumber에 따라 입력, 조회, 수정, 삭제, 종료를 선택하려 할때
		
		int jopnumber = 3;
		switch( jopnumber ) {
		case 1:
			System.out.println("입력작업을 수행합니다...");
			break; //값이정해지면 case구문 밖으로 이동
		case 2:
			System.out.println("조회작업을 수행합니다...");
			break;
		case 3:
			System.out.println("수정작업을 수행합니다...");
			break;
		case 4:
			System.out.println("삭제작업을 수행합니다...");
			break;
		case 5:
			break;
		default:
			System.out.println("잘못된 선택입니다.");
			break;
	}//switch
		System.out.println("");
		
		
	}//main
	
}//class