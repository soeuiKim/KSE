package lesson002;

public class MemberArrayListTest {

	public static void main(String[] args) {
		
		MemberArrayList memberArrayList = new MemberArrayList();
		
		Member memberLee = new Member(1001,"이지원");
		Member memberSon = new Member(1002,"손민국");
		Member memberPark = new Member(1003,"박서원");
		Member memberHong = new Member(1004,"홍길동");
		
		memberArrayList.addMember(memberLee);
		memberArrayList.addMember(memberSon);
		memberArrayList.addMember(memberPark);
		memberArrayList.addMember(memberHong);
		
		// 멤버 추가 후 전체 멤버 확인
		memberArrayList.showAllMember();
		
		// 멤버 하나 삭제
		memberArrayList.removeMember(memberHong.getMemberId());
		
		// 삭제 후 전체 멤버 확인
		memberArrayList.showAllMember();
		
		
	}//main

}//class
