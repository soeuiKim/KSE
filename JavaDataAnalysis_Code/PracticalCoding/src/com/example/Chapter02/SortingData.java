package com.example.Chapter02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;
import java.util.TreeMap;

public class SortingData {

	public static void main(String[] args) {
		 File file = new File("data/Countries_sorting.dat");
	        TreeMap<String,Integer> dataset = new TreeMap();
	        try {
	            Scanner input = new Scanner(file);
	            while (input.hasNext()) {
	                String x = input.next();
	                int y = input.nextInt();
	                dataset.put(x, y);
	            }
	            input.close();
	        } catch (FileNotFoundException e) {
	            System.out.println(e);
	        }
	        print(dataset);
	    }
	    
	public static void print(TreeMap<String, Integer> map) {
		for (String key : map.keySet()) {
			System.out.printf("%-16s  %,12d  %n", key, map.get(key));
	        }
		}
}
