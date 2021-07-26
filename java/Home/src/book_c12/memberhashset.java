package book_c12;

import java.util.HashSet;
import java.util.Iterator;

public class memberhashset {
	
	private HashSet<member> hashset;
	
	public memberhashset() {
		hashset = new HashSet<member>();
	}
	
	public void addmember(member member) {
		hashset.add(member);
	}
	
	public boolean removemember(int memberId) {
		Iterator<member> ir = hashset.iterator();
		
		while(ir.hasNext()) {
			member member = ir.next();
			int tempId = member.getMemberId();
			
			if(tempId == memberId) {
				hashset.remove(member);
				return true;
			}
		}
		
		System.out.println(memberId + "가 존재하지 않습니다.");
		return false;
		
	}//removemember
	
	public void showAllmember() {
		for(member member : hashset) {
			System.out.println(member);
		}
		System.out.println("-----");
	}
	
}//end of class
