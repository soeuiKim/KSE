package lesson001;

import java.util.ArrayList;
import java.util.Iterator;

public class E017_ArrayList {

	public static void main(String[] args) {
		// 기존 배열의 단점
		// 1. 항상 배열의 길이를 정하고 시작해야 한다.
		// 2. 배열을 사용하는 중에 배열 길이를 변경할 수 없다.
		// 3. 배열 요소를 추가하거나 삭제하기 불편하다.
		//   기존요소 위치를 변경하여야 하기 때문에 
		// 
		// 객체배열을 좀더 쉽게 사용하기 위한 클래스를 제공
		// ===> ArrayList 클래스 
		// 객체배열을 관리할 수 있는 멤버 변수와 메서드를 제공
		// 상세한 내용은 교재 12장에서 설명.
		
		// 객체_object : 현신세계에 존재하는 모든 사물 또는 개념
		// 클래스_class: (객체의 집합)
		
		// 클래스를 이용하여 객체 생성 _ example ▼
//		E018_Book book1 = new E018_Book("자바프로그래밍","홍길동");
//		book1.showInfo();
//		E018_Book book2 = new E018_Book("빅데이터분석","김갑순");
//		book2.showInfo();
		
		//배열을 이용
//		E018_Book[] books = new E018_Book[5];
//		books[0] = new E018_Book("자바프로그래밍","홍길동");
//		books[1] = new E018_Book("파이썬 프로그래맹","김갑순");
//		books[2] = new E018_Book("C/C++ 프로그래밍","춘향이");
//		books[3] = new E018_Book("Html 프로그래밍","황진이");
//		books[4] = new E018_Book("JSP 프로그래맹","박문수");
//		
//		for(E018_Book book : books) {
//			book.showInfo();
//		}
//		
//		System.out.println("--------------------------");
//		books[2].setTitle("(개정판)C++ 프로그래밍");
//		
//		for(E018_Book book : books) {
//			book.showInfo();
//		}
		
		// ArrayList 이용
		// 배열의 추가, 병경이 용이함을 확인
		// Sysntax : 
		// ArrayList<E> 배열이름 = new ArrayList<E>();
		//           ▲ 제너릭 : 일반적인 클래스를 넣을수 있음
		//           E :  제너릭 자료형으로 보통 사용자가 정의한 클래스 또는 
		//                자바의 기본 클래스형을 의미한다.
		
		ArrayList<E018_Book> books = new ArrayList<E018_Book>();
		// ArrayList 좋은점 : 다이내믹함ㅎㅎ
		//                    데이터 사이즈만큼만 저장공간확보

		books.add(new E018_Book("자바1 프로그래밍","홍길동"));
		books.add(new E018_Book("자바2 프로그래밍","홍길동"));
		books.add(new E018_Book("자바3 프로그래밍","홍길동"));
		books.add(new E018_Book("자바4 프로그래밍","홍길동"));
		books.add(new E018_Book("자바6 프로그래밍","홍길동"));
		books.add(new E018_Book("자바7 프로그래밍","홍길동"));
		books.add(new E018_Book("자바8 프로그래밍","홍길동"));
		books.add(new E018_Book("자바9 프로그래밍","홍길동"));
		books.add(new E018_Book("자바10 프로그래밍","홍길동"));
		
		
		for(E018_Book book : books) {
			book.showInfo();
		}
		
		System.out.println("======index 지정, 데이터 추가======");
		
		//끼워넣기
		books.add(4, new E018_Book("자바5 프로그래밍","춘향이"));
		
		for(E018_Book book : books) {
			book.showInfo();
		}
		
		//지우기
		System.out.println("=========remove test==========");
		
		books.remove(7);
		
		for(E018_Book book : books) {
			book.showInfo();
		}
		
		
		
	}//main

}//class
