package book_c12;

public class memberhashsetTest {

	public static void main(String[] args) {
		
		memberhashset memberhashset = new memberhashset();
		
		member memberLee = new member(1001, "이지원");
		member memberSon = new member(1002, "손민국");
		member memberPark = new member(1003, "박서훤");
		
		memberhashset.addmember(memberLee);
		memberhashset.addmember(memberSon);
		memberhashset.addmember(memberPark);
		memberhashset.showAllmember();
		
		member memberHong = new member(1003, "홍길동");
		memberhashset.addmember(memberHong);
		memberhashset.showAllmember();
		
	}

}
