package lesson002;

import java.util.Iterator;
import java.util.LinkedList;
import java.util.PriorityQueue;
import java.util.Queue;

public class Aque {

	public static void main(String[] args) {
		
//		// 큐의 링크드리스트 생성
//		Queue<String> animal1 = new LinkedList<>();
//
//		// 큐의 배열
//		Queue<String> animal2 = new ArrayDeque<>();
//
//		// 큐의 Priority(우선순위)큐
//		Queue<String> animal3 = new PriorityQueue<>();
		
		
		// 링크드리스트
        Queue<Integer> numbers = new LinkedList<>();

        // 값 넣기
        numbers.offer(1);
        numbers.offer(2);
        numbers.offer(3);
        System.out.println("Queue: " + numbers);

        // peek() : 헤드 반환
        int accessedNumber = numbers.peek();
        System.out.println("Accessed Element: " + accessedNumber);

        // poll() : 헤드를 반환하고 제거
        int removedNumber = numbers.poll();
        System.out.println("Removed Element: " + removedNumber);
        
        //제거되고 남은 값들
        System.out.println("Updated Queue: " + numbers);
		
        
        System.out.println("=========================");
        
		
       // 우선순위 큐
        PriorityQueue<Integer> number = new PriorityQueue<>();
        
        // 값넣기_ 큐가가득차면 예외발생
        number.add(4);
        number.add(2);
        System.out.println("PriorityQueue: " + number);

        // offer() : 지정된 요소를 큐에 넣기
        number.offer(1);
        System.out.println("Updated PriorityQueue: " + number);
        
        // remove() : 지우기
        boolean result = number.remove(2);   //?
        System.out.println("제거됨? " + result);   

        // poll() : 헤드반환후 제거
        int num = number.poll();
        System.out.println("poll() 로 지운 것 : " + num);
        
        
        
        
        
        
        
        
        
        
        
        System.out.println("=========================");
        
        
        
        
        
        
        
        
        
        
		
		
	}//maim

}//class
