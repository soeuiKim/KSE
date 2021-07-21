package lesson002;

public class Member {
	
	private int memberId; //회원 아이디
	private String memberName; //회원 이름
	
	 // ▼ 이런 형태를 method 메소드 (Function_c언어에서는)
	 // public 이름 () { .... }
	        // 메소드중에서도 클래스 이름과 같은 이름을 가지는 것들을
	        // (constructor)생성자라고 한다
	public Member(int memberId, String memberName) {
		this.memberId = memberId;  //this : 클래스에 생성된 객체의
		this.memberName = memberName;
	}
	
	// getters & setters _ 오른쪽버튼 - 소스 - 제너레이트...
	public int getMemberId() {
		return memberId;
	}

	public void setMemberId(int memberId) {
		this.memberId = memberId;
	}

	public String getMemberName() {
		return memberName;
	}

	public void setMemberName(String memberName) {
		this.memberName = memberName;
	}

	// 마우스오른쪽 - 소스 - override/implement methods - hashCode 체크
	//                                  -after to string
	@Override
	public String toString() {
		return memberName + " 회원님의 아이디는 " + memberId + " 입니다. ";
	}
	
	
	
	
	
} // end of class
