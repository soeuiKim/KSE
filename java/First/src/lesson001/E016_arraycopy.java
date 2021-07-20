package lesson001;

import java.util.Arrays;

public class E016_arraycopy {

	public static void main(String[] args) {
		
		int [] numbers = {1, 2, 3, 4, 5, 6};
        int [] positiveNumbers = numbers;    // 배열 복사

        for (int number: positiveNumbers) {
            System.out.print(number + ", ");
        }
        
        System.out.println();
		System.out.println("numbers :         " + numbers);
		System.out.println("positiveNumbers : " + positiveNumbers);
		System.out.println();
		System.out.println();
		// ▲ shallow copy 얕은 복사
		// 복사본이 원본에 영향을준다
		// <-> 반대개념 deep copy 깊은 복사
		// ▼ 복사본과 원본이 다른 개념인것.
		
		 int [] source = {1, 2, 3, 4, 5, 6};
	     int [] destination = new int[6];

	     // iterate and copy elements from source to destination
	     for (int i = 0; i < source.length; ++i) {
	    	 destination[i] = source[i];
	     }
	     
	     
	     System.out.println("source :");
	     System.out.println(source);
	     System.out.println(Arrays.toString(source));
	     
	     System.out.println();
	     System.out.println();
	     
	     System.out.println("destination :");
	     System.out.println(destination);
	     System.out.println(Arrays.toString(destination));
	     
	     System.out.println();
	     System.out.println();
	     
	     destination[0] = 1000;
	     System.out.println("변경후 두 배열값 비교 :");
	     System.out.println(Arrays.toString(source));
	     System.out.println(Arrays.toString(destination));
	     
	     System.out.println();
	     System.out.println();
	     
	     // 복사 방법 3 _ arraycopy() 사용
	     
	     //arraycopy(Object src, int srcPos,Object dest, int destPos, int length)
	     //       소스배열   배열시작위치  복사대상배열   대상배열시작위치  복사할요소의 수
	     
	     int[] n1 = {2, 3, 12, 4, 12, -2};
	      
	     int[] n3 = new int[5];

	     // Creating n2 array of having length of n1 array
	     // n1길이만큼 배열 n2 생성
	     int[] n2 = new int[n1.length];

	     // copying entire n1 array to n2
	     //              소스n1의0번째,n2의 0번째에 n1의 길이만큼
	     System.arraycopy(n1, 0, n2, 0, n1.length);
	     System.out.println("n2 = " + Arrays.toString(n2));  

	     // copying elements from index 2 on n1 array
	     // copying element to index 1 of n3 array
	     // 2 elements will be copied
	     System.arraycopy(n1, 2, n3, 1, 2);
	     System.out.println("n3 = " + Arrays.toString(n3));  
	     
	     
	     
	}//main

}//class
