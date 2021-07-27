package lesson002;

import java.util.HashSet;
import java.util.Iterator;
import java.util.TreeSet;

public class ASet {

	public static void main(String[] args) {
		
		 HashSet<Integer> nb = new HashSet<>();
		 nb.add(2);
		 nb.add(5);
		 nb.add(6);
		 System.out.println("HashSet: " + nb);

		 // iterator()
		 Iterator<Integer> iterate = nb.iterator();
		 System.out.print("HashSet using Iterator: ");

		 // 요소 엑세스
		 while(iterate.hasNext()) {
			 System.out.print(iterate.next());
			 System.out.print(", ");
		 }//while

		 System.out.println();
		 System.out.println("--------------");

		 HashSet<Integer> evNb = new HashSet<>();
		 evNb.add(2);
		 evNb.add(4);
		 System.out.println("evNb: " + evNb + "    nb : " + nb);

		 // addAll() : Union합집합
		 nb.addAll(evNb);
		 System.out.println("Union is: " + nb);

		 System.out.println();
		 System.out.println("--------------");

		 HashSet<Integer> prnb = new HashSet<>();
		 prnb.add(2);
		 prnb.add(3);
		 System.out.println(" prnb : " + prnb);
		 System.out.println(" evNb : " + evNb);

		 // retainAll() : Intersection교집합
		 evNb.retainAll(prnb);
		 System.out.println("Intersection(교집합) : " + evNb);


		 System.out.println();
		 System.out.println("--------------");

		 
		 // containsAll() : 부분집합인지 확인하기
		 HashSet<Integer> nbs = new HashSet<>();
		 nbs.add(2);
		 nbs.add(3);
		 nbs.add(4);
		 nbs.add(5);
		 System.out.println(" nbs : " + nbs);
		 System.out.println(" prnb : " + prnb);
		 
		 boolean result = nbs.containsAll(prnb);
		 System.out.println(" prnb는 nbs의 부분집합인가? " + result);
		 
		 System.out.println();
		 System.out.println("--------------");
		 
		 TreeSet<Integer> numbers = new TreeSet<>();
		 numbers.add(2);
		 numbers.add(4);
		 numbers.add(6);
		 numbers.add(8);
		 System.out.println("TreeSet: " + numbers);

		 // higher() : 지정요소보다 큰 요소중에 가장작은값
		 System.out.println("Using higher: " + numbers.higher(6));

		 // lower() : 지정요소보다 작은 요소중에 가장큰것
		 System.out.println("Using lower: " + numbers.lower(6));

		 // ceiling() : 나를포함해서 지정요소보다 큰값중에 가장작은거
		 System.out.println("Using ceiling: " + numbers.ceiling(3));

		 // floor() : 나를포함하여 지정요소보다 작은값중에 가장큰거
		 System.out.println("Using floor: " + numbers.floor(6));

		 
		 
		 
		 	
	       
		
	}//main

}//class
