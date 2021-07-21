package lesson002;

import java.util.LinkedList;

public class LinkedListTest {

	public static void main(String[] args) {
		
	// LinkedList의 이해와 활용
		LinkedList<String> mylist = new LinkedList<String>();
		
		mylist.add("a");
		mylist.add("b");
		mylist.add("c");
		
		System.out.println("---a,b,c추가후 출력---");
		System.out.println(mylist);
		
		System.out.println();//줄바꿈
		System.out.println("---d 추가후 전체 출력---");
			
		mylist.add(1,"d"); // 인덱스 1 위치에 d 추가
		System.out.println(mylist);
		
		System.out.println();//줄바꿈
		System.out.println("---0추가후 출력---");
		mylist.addFirst("0"); //맨 앞자리에 0 추가
		System.out.println(mylist);
		
		System.out.println();//줄바꿈
		System.out.println("---맨뒤 요소 삭제후 출력---");
		System.out.println(mylist.removeLast());
		                    //연결된 리스트의 맨뒤 요소 삭제 후 해당 요소 출력
		System.out.println(mylist);
	
		
	}//end of main

}//end of class
