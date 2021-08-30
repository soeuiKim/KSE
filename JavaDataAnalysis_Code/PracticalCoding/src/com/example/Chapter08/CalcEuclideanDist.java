package com.example.Chapter08;

import org.apache.poi.util.SystemOutLogger;

public class CalcEuclideanDist {

	public static void main(String[] args) {
		// 3차원 좌표공간상의 두 점 사이의 거리
		double[] a = {-1, 2, 3};
		double[] b = {4, 0, -3};
		
		// 2차원 좌표공간상의 두 점 사이의 거리
//		double[] a = {1,3};
//		double[] b = {5,6};
		
		calcEuclideanDist(a,b);

	}// end of main
	
	public static void calcEuclideanDist(double[] a, double[] b) {
		double sum = 0;
		for(int i = 0; i < a.length; i++) {
			sum += Math.pow(a[i]-b[i], 2);
		}
		double distance = Math.sqrt(sum);
		System.out.println("두 점 사이의 거리는 : " + distance);
	}
	
	
}// end of class
