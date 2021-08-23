package com.example.Chapter02;

import java.util.Scanner;

public class Country {
	protected String name;
	protected int population;

	public Country(Scanner in) {
		if (in.hasNextLine()) {
			this.name = in.next();
			this.population = in.nextInt();
		}
	}
	
	@Override
	public String toString() {
		return String.format("%-10s %, 12d", name,population);
	}

}
