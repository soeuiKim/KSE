package book_c12;

import java.util.LinkedList;

public class linkedlistTest {

	public static void main(String[] args) {
					
		LinkedList<String> mylist = new LinkedList<String>();
		
		mylist.add("A");
		mylist.add("B");
		mylist.add("C");
		
		System.out.println(mylist);
		
		mylist.add(1, "D");
		
		System.out.println(mylist);
		
		mylist.addFirst("0");
		
		System.out.println(mylist);
		
		System.out.println(mylist.removeLast());
		
		System.out.println(mylist);
		
		
	}

}
