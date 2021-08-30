/*  Data Analysis with Java
 *  John R. Hubbard
 *  Jul 20, 2017
 */

package dawj.ch09;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Comparator;
import java.util.Scanner;
import java.util.Set;
import java.util.TreeSet;

public class Recommender2 {
    private static int m;         //  사용자 수
    private static int n;         //  아이템 수
    private static int[][] u;     // 유틸리티 행렬
    private static double[][] s;  // 유사도 행렬
    private static int user;      // 현재 사용자
    private static Item itemBought;    // 사용자가 구매한 현재 아이템

    public static void main(String[] args) {
        readFiles();
        getInput();
        Set<Item> set1 = itemsNotYetBought();
        Set<Item> set2 = firstPartOf(set1, n/3);
        makeRecommendations(set2, n/4);
    }

    public static void readFiles() {
        File utilityFile = new File("data/Utility1.dat");
        File similarityFile = new File("data/Similarity1.dat");
        try {
            readUtilMatrix(utilityFile);
            readSimilMatrix(similarityFile);
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }
    
    public static void readUtilMatrix(File f) throws FileNotFoundException {
        Scanner in = new Scanner(f);
        m = in.nextInt();  in.nextLine();
        n = in.nextInt();  in.nextLine();
        u = new int[m+1][n+1];
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                u[i][j] = in.nextInt();
            }
            in.nextLine();
        }
        in.close();
    }
    
    public static void readSimilMatrix(File f) throws FileNotFoundException {
        Scanner in = new Scanner(f);
        n = in.nextInt();    
        in.nextLine();
        s = new double[n+1][n+1];
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                s[j][k] = in.nextDouble();
            }
            in.nextLine();
        }
        in.close();
    }

    public static void getInput() {
        Scanner input = new Scanner(System.in);
        System.out.print("사용자 번호 입력: ");
        user = input.nextInt();
        System.out.print("아이템 번호 입력: ");
        int bought = input.nextInt();
        if (u[user][bought] == 1) {
            System.out.printf("사용자 %d(이)가 이미 아이템%d(을)를 구매했음.%n", user, bought);
            System.exit(0);
        }
        System.out.printf("사용자 %d(이)가 아이템 %d(을)를 구매함.%n", user, bought);
        u[user][bought] = 1;
        itemBought = new Item(bought);
    }
        
    private static Set<Item> itemsNotYetBought() {
        Set<Item> set = new TreeSet(itemBought.new SimilarityComparator());
        for (int j = 1; j <= n; j++) {
            if (u[user][j] == 0) {  // 사용자가 아직 구매하지 않은 아이템 j
                set.add(new Item(j));
            }
        }
        return set;
    }
        
    private static Set<Item> firstPartOf(Set<Item> set1, int n1) {
        Set<Item> set2 = new TreeSet(itemBought.new PopularityComparator());
        int count = 0;
        for (Item item : set1) {
            set2.add(item);
            if (++count == n1) {
                break;
            }
        }
        return set2;
    }

    private static void makeRecommendations(Set<Item> set, int n2) {
        System.out.printf("추천하는 아이템 %d개:", n2);
        int count = 0;
        for (Item item : set) {
            System.out.printf("  %d", item.index);
            if (++count == n2) {
                break;
            }
        }
        System.out.println();
    }

    static class Item {
        int index;
        
        public Item(int index) {
            this.index = index;
        }
        
        public int popularity() {
            int sum = 0;
            for (int i = 1; i <= m; i++) {
                sum += u[i][this.index];
            }
            return sum;
        }
        
        public double similarity(Item item) {
            return s[this.index][item.index];
        }

        public class PopularityComparator implements Comparator<Item> {
        	
            public int compare(Item item1, Item item2) {
                int p1 = item1.popularity();
                int p2 = item2.popularity();
                return (p1 > p2 ? -1 : 1);
            }
        }
        
        public class SimilarityComparator implements Comparator<Item> {
        	
            public int compare(Item item1, Item item2) {
                double s1 = Item.this.similarity(item1);
                double s2 = Item.this.similarity(item2);
                return (s1 > s2 ? -1 : 1);
            }
        }
        
        @Override
        public String toString() {
            return String.format("%d", index);
        }
    }
}

/*
run:
Enter user number: 1
Enter item number: 1
User 1 bought item 1.
	set1 = [2, 12, 6, 9]
	set2 = [12, 9, 2, 6]
We also recommend these 3 items:  12  9  2
run:
Enter user number: 4
Enter item number: 1
User 4 bought item 1.
	set1 = [2, 12, 6, 3, 4, 10, 11, 8]
	set2 = [12, 3, 2, 6]
We also recommend these 3 items:  12  3  2
*/
