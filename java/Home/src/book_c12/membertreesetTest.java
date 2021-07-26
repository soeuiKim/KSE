package book_c12;

public class membertreesetTest {

	public static void main(String[] args) {
		membertreeset membertreeset = new membertreeset();
		
		
		member memberPark = new member(1003, "박서훤");
		member memberLee = new member(1001, "이지원");
		member memberSon = new member(1002, "손민국");
		
		
		membertreeset.addmember(memberLee);
		membertreeset.addmember(memberSon);
		membertreeset.addmember(memberPark);
		membertreeset.showAllmember();
		
		member memberHong = new member(1003, "홍길동"); 
		
		membertreeset.addmember(memberHong);
		membertreeset.showAllmember();

	}

}
