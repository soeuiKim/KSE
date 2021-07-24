package book_c12;

import java.util.ArrayList;

public class queue {
	
	private ArrayList<String> arrayqueue = new ArrayList<String>();
	
	public void enQueue(String data) {
		arrayqueue.add(data);
	}
	
	public String deQueue() {
		int len = arrayqueue.size();
		if( len == 0 ) {
			System.out.println("큐가 비었습니다.");
			return null;
		}
		return (arrayqueue.remove(0));
	}
	
	
	public static void main(String[] args) {
		
		queue que = new queue();
		
		que.enQueue("A");
		que.enQueue("B");
		que.enQueue("C");
		System.out.println(que);
		
		System.out.println(que.deQueue());
		System.out.println(que.deQueue());
		System.out.println(que.deQueue());
		
		
		
	}//end of main

}//end of class
