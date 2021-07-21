package lesson002;

public class MemberHashMapTest {

	public static void main(String[] args) {
		MemberHashMap memberHashMap = new MemberHashMap();
		
		Member Member1 = new Member(1001,"홍길동1");
		Member Member2 = new Member(1002,"홍길동2");
		Member Member3 = new Member(1003,"홍길동3");
		Member Member4 = new Member(1004,"홍길동4");
		
		memberHashMap.addMember(Member1);
		memberHashMap.addMember(Member2);
		memberHashMap.addMember(Member3);
		memberHashMap.addMember(Member4);
		
		System.out.println("---4개 데이터 추가후 전체 출력---");
		memberHashMap.showAllMember();
		
		System.out.println("---1개 데이터 삭제추 전체 출력---");
		memberHashMap.removeMember(1003);
		memberHashMap.showAllMember();
		

	}

}
