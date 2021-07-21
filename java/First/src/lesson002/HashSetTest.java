package lesson002;

import java.util.HashSet;

public class HashSetTest {

	public static void main(String[] args) {
		// set 인터페이스를 이해하고 활용할 수 있다.
		HashSet<String> hashset = new HashSet<String> ();
		
		hashset.add(new String("임정순")); // ← 확실한 입력을위해 new사용
		hashset.add("박현정"); // new 아니어도 입력가능
		hashset.add("박현정"); //중복x
		System.out.println(hashset);

	}

}
