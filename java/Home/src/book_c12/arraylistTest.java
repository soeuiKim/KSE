package book_c12;

public class arraylistTest {

	public static void main(String[] args) {
		
		arraylist memberarraylist = new arraylist();
		
		member memberLee = new member(1001, "이지원");
		member memberSon = new member(1002, "손민국");
		member memberPark = new member(1003, "박서훤");
		member memberHong = new member(1004, "홍길동");
		
		
		memberarraylist.addMember(memberLee);
		memberarraylist.addMember(memberSon);
		memberarraylist.addMember(memberPark);
		memberarraylist.addMember(memberHong);
		
		memberarraylist.showAllMember();
		
		memberarraylist.removeMember(memberHong.getMemberId());
		memberarraylist.showAllMember();
		
		
	
		
	}//end of main

}//end of class
