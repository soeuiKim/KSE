package lesson002;

public class BStudent extends BPerosn {
	
	String studentId;
	
	public BStudent(String studentId) {
		this.studentId = studentId;
		this.name = "누구쇼";
		this.address = "어디사쇼";
	}
	
	public BStudent(String name, String address, String studentId) {
		this.studentId = studentId;
		this.name = name;
		this.address = address;
	}
	
	public void learn(String subject) {
		System.out.println(name + "은(는)" + subject + "을(를) 공부합니다");
	}
	
	@Override
	public void showinfo() {
		System.out.println(studentId + "," + name + ":" + address);
	}
	
	
}//class
