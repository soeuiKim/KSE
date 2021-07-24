package book_c12;

import java.util.TreeSet;

public class treesetTest {

	public static void main(String[] args) {
		
		TreeSet<String> treeset = new TreeSet<String>();
		
		treeset.add("홍길동");
		treeset.add("강감찬");
		treeset.add("이순신");
		
		for(String str : treeset) {
			System.out.println(str);
		}
		
	}

}
