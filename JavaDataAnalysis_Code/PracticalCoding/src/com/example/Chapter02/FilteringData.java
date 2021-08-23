package com.example.Chapter02;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.HashSet;
import java.util.Scanner;
import java.util.Set;

public class FilteringData {
	private static final int MIN_pop = 7000000;
	
	public static void main(String[] args) {
		File file = new File("data/Countries.dat");
		Set<Country> dataset = readDataset(file);
		
		for (Country country : dataset) {
			if (country.population >= MIN_pop) {
				System.out.println(country);
			}
		}
	}
	public static Set readDataset(File file) {
		Set<Country> set = new HashSet();
		try {
			Scanner input = new Scanner(file);
			input.nextLine();
			while (input.hasNextLine()) {
				set.add(new Country(input));
			}
			input.close();
		} catch (FileNotFoundException e) {
			System.out.println(e);
		}
		return set;
	}
	
	
	
}
