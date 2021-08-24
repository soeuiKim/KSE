//package com.example.Chapter02;
//
//import java.io.File;
//import java.io.FileNotFoundException;
//import java.io.PrintWriter;
//import java.util.Scanner;
//
//public class MergingFiles {
//
//	public static void main(String[] args) {
//		File inFile1 = new File("data/Countries_sorting.dat");
//		File inFile2 = new File("data/Countries_merging.dat");
//		File outFile = new File("data/countriesMerged.dat");
//		try {
//			Scanner in1 = new Scanner(inFile1);
//			Scanner in2 = new Scanner(inFile2);
//			PrintWriter out = new PrintWriter(outFile);
//			Country2_ country1 = new Country2_(in1);
//			Country2_ country2 = new Country2_(in2);
//			System.out.println(country1.hashCode());
//            System.out.println(country2.hashCode());
//			while (!country1.isNull() && !country2.isNull()) {
//				if (country1.compareTo(country2) < 0) {
//					out.println(country1);
//					country1 = new Country2_(in1);
//				} else {
//					out.println(country2);
//					country2 = new Country2_(in2);
//				}
//				while (!country1.isNull()) {
//	                out.println(country1);
//	                country1 = new Country2_(in1);
//	            }
//	            while (!country2.isNull()) {
//	                out.println(country2);
//	                country2 = new Country2_(in2);
//	            }
//	            in1.close();
//	            in2.close();
//	            out.close();
//	        } catch (FileNotFoundException e) {
//	            System.out.println(e);
//			}
//		}
//
//	}
//
//}
