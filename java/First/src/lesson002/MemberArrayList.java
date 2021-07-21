package lesson002;

import java.util.ArrayList;

public class MemberArrayList {
	
	private ArrayList<Member> arrayList;
	
	// constructor 생성자
	public MemberArrayList() {
		arrayList = new ArrayList<Member>();
	}//end of constructor MemberArrayList()
	
	// arrayList에 파라미터로 전달받은 멤버를 add추가한다.
	//     실행하지 않아도 될때 void
	public void addMember(Member member) {
		arrayList.add(member);
	}// end of addMember
	
	//    
	public boolean removeMember(int memberId) {
		for(int i = 0; i < arrayList.size( ); i++) {
			Member member = arrayList.get(i);
			int tempId = member.getMemberId();
			if(tempId == memberId) {
				arrayList.remove(i);
				return true;
			}//end of if(tempId == memberId)
		}//end of for(int i = 0....)
		
		System.out.println(memberId + "가 존재하지 않습니다.");
		return false;
		
	}// end of removeMember()
	
	public void showAllMember() {
		for(Member member : arrayList) {
			System.out.println(member);
		}
		System.out.println("-----");
	}
	
	
	
}//class
