package lesson002;

import java.util.Stack;

public class EStackTest {

	public static void main(String[] args) {
		Stack<String> stack = new Stack<String>();
		
		// stack.push 와 같은 결과물
		stack.add("JAVA");     // add는 list의 하위이기때문에 사용가능
		stack.add("Python");
		stack.add("Funny");
		
		System.out.println("origin Stack : " + stack);
		
		String temp = stack.peek();
		System.out.println(temp);
		System.out.println("Stack after peek() : " + stack);
		
		// search() : 값을 찾아 위치값(1 base)을 반환
		int idx = stack.search("Python");
		System.out.println("idx of python   :    " + idx);
		
		temp = stack.pop();
		System.out.println(temp);
		System.out.println("Stack after pop() : " + stack);
		
		int ids = stack.search("Python");
		System.out.println("idx of python   :    " + ids);
		
		
		
		
		
	}//main

}//class
