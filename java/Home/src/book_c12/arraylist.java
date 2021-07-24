package book_c12;

import java.util.ArrayList;    

public class arraylist {
	private ArrayList<member> arraylist;  

	public arraylist(){
		arraylist = new ArrayList<member>();  
	}
	
	public void addMember(member member){  
		arraylist.add(member);
	}
	
	public boolean removeMember(int memberId){ 
		
		for(int i =0; i<arraylist.size(); i++){ 
			member member = arraylist.get(i);
			int tempId = member.getMemberId();
			if(tempId == memberId){            
				arraylist.remove(i);           
				return true;                  
			}
		}
				
		System.out.println(memberId + "가 존재하지 않습니다"); 
		return false;                   
	}
	
	public void showAllMember(){
		for(member member : arraylist){
			System.out.println(member);
		}
		System.out.println();
	}

}
