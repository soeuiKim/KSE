/*  Data Analysis with Java
 *  John R. Hubbard
 *  July 22, 2017
 */

package dawj.ch09;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Filter3 {
    private static int m;  //  사용자 수
    private static int n;  //  아이템 수

    public static void main(String[] args) {
        File purchasesFile = new File("data/Purchases3.dat");
        File utilityFile = new File("data/Utility3.dat");
        File similarityFile = new File("data/Similarity3.dat");
        try {
            double[][] u = computeUtilityMatrix(purchasesFile);
            storeUtilityMatrix(u, utilityFile);
            double[][] s = computeSimilarityMatrix(u);
            storeSimilarityMatrix(s, similarityFile);
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }
    
    public static double[][] computeUtilityMatrix(File file) 
            throws FileNotFoundException {
        Scanner in = new Scanner(file);
        // 다섯줄의 헤더 라인을 먼저 읽는다.
        m = in.nextInt();  in.nextLine();
        n = in.nextInt();  in.nextLine();
        in.nextLine();  in.nextLine();  in.nextLine();

        //  유틸리티 행렬을 읽는다.
        double[][] u = new double[m+1][n+1];
        while (in.hasNext()) {
            int i = in.nextInt();       // 사용자
            int j = in.nextInt();       // 아이템
            u[i][j] = in.nextDouble();  // 등급
        }
        in.close();
        return u;
    }

    public static void storeUtilityMatrix(double[][] u, File file)
            throws FileNotFoundException {
        PrintWriter out = new PrintWriter(file);
        out.printf("%d 사용자%n", m);
        out.printf("%d 아이템%n", n);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                out.printf("%5.1f", u[i][j]);
            }
            out.println();
        }
        out.close();
    }
    
    public static double[][] computeSimilarityMatrix(double[][] u) {
        double[][] s = new double[n+1][n+1];
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= n; k++) {
                s[j][k] = cosine(u, j, k);
            }
        }
        return s;
    }

    public static void storeSimilarityMatrix(double[][] s, File file)
            throws FileNotFoundException {
        PrintWriter out = new PrintWriter(file);
        out.printf("%d items%n", n);
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= n; j++) {
                out.printf("%6.2f", s[i][j]);
            }
            out.println();
        }
        out.close();
    }

    /*  u[][]의 j 와 k 번째 열의 코사인 유사도를 반환한다.
     */
    public static double cosine(double[][] u, int j, int k) {
        double denominator = norm(u,j)*norm(u,k);
        return (denominator == 0 ? 0 : dot(u,j,k)/denominator);
    }
    
    /*  u[][]의 j와 k 번째 열의 내적을 반환한다.
     */
    public static double dot(double[][] u, int j, int k) {
        double sum = 0.0;
        for (int i = 0; i <= m; i++) {
            sum += u[i][j]*u[i][k];
        }
        return sum;
    }
    
    /*  u[][]의 j와 k 번째 열의 노름을 반환한다.
     */
    public static double norm(double[][] u, int j) {
        return Math.sqrt(dot(u,j,j));
    }
}
