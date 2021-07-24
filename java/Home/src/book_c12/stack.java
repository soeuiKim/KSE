package book_c12;

import java.util.ArrayList;

public class stack {
	
	private ArrayList<String> arraystack = new ArrayList<String>();
	
	public void push(String data) {
		arraystack.add(data);
	}
	
	public String pop() {
		int len = arraystack.size();
		if( len == 0 ) {
			System.out.println("스택이 비었습니다.");
			return null;
		}
		return (arraystack.remove(len-1));
	}

	
	// test
	public static void main(String[] args) {

		stack stack = new stack();
		stack.push("A");
		stack.push("B");
		stack.push("C");
		
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		System.out.println(stack.pop());
		
	}
}


