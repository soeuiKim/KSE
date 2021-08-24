package com.example.Chapter02;

import java.util.Scanner;

public class Country2_ { // implements comparable {
	protected String name;
	protected int population;

	public Country2_(Scanner in) {
		if (in.hasNextLine()) {
			this.name = in.next();
			this.population = in.nextInt();
		}
	}
	
	public boolean isNull() {
		return this.name ==null;
	}
	
//	@Override
//	public int compareTo(Object object) {
//		Country that = (Country) object;
//		return this.population - that.population;
//	}
	
	@Override
	public String toString() {
		return String.format("%-10s %, 12d", name,population);
	}

}
