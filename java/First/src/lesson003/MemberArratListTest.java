package lesson003;

import lesson002.Member;
import lesson002.MemberArrayList;

public class MemberArratListTest {

	public static void main(String[] args) {
		// 김소의
		
		MemberArrayList memberArrayList = new MemberArrayList();
		
		Member memberLee = new Member(1001,"이지원");
		Member memberSon = new Member(1002,"손민국");
		Member memberPark = new Member(1003,"박서원");
		Member memberHong = new Member(1004,"홍길동");
		
		memberArrayList.addMember(memberLee);
		memberArrayList.addMember(memberSon);
		memberArrayList.addMember(memberPark);
		memberArrayList.addMember(memberHong);
		
	
		memberArrayList.showAllMember();
		
		
		memberArrayList.removeMember(memberHong.getMemberId());
		
		
		memberArrayList.showAllMember();

	}

}
