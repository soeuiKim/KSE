package book_c12;

import java.util.Iterator;
import java.util.TreeSet;

public class membertreeset {
	
	private TreeSet<member> treeset;
	
	public membertreeset() {
		treeset = new TreeSet<member>();
	}
	
	public void addmember(member member) {
		treeset.add(member);
	}
	
	public boolean removemember(int memberId) {
		Iterator<member> ir = treeset.iterator();
		
		while (ir.hasNext()) {
			member member = ir.next();
			int tempId = member.getMemberId();
			if(tempId == memberId) {
				treeset.remove(member);
				return true;
				}
			}
			System.out.println(memberId + "가 존재하지 않습니다.");
			return false;
		}//end boolean removemember
		
		public void showAllmember() {
			for(member member : treeset) {
				System.out.println(member);
			}
			System.out.println("=====");
			}//end showallmember
		
	}//end class
