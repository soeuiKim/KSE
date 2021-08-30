/*  Data Analysis with Java
 *  John R. Hubbard
 *  July 22, 2017
 */

package dawj.ch09;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.IOException;
import java.io.PrintWriter;
import java.io.RandomAccessFile;
import java.util.Scanner;

public class Filter4 {
    private static int m;  //  사용자 수
    private static int n;  //  아이템 수
    
    private static final int W = Double.BYTES;  // 8

    public static void main(String[] args) {
        File purchasesFile = new File("data/Purchases3.dat");
        File utilityFile = new File("data/Utility3.dat");
        File similarityFile = new File("data/Similarity3.dat");
        try {
            SparseMatrix u = computeUtilityMatrix(purchasesFile);
            storeUtilityMatrix(u, utilityFile);
            double[][] s = computeSimilarityMatrix(u);
            storeSimilarityMatrix(s, similarityFile);
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }
    
    public static SparseMatrix computeUtilityMatrix(File file) 
            throws FileNotFoundException {
        Scanner in = new Scanner(file);
        // 다섯줄의 헤더 라인을 먼저 읽는다.
        m = in.nextInt();  in.nextLine();
        n = in.nextInt();  in.nextLine();
        in.nextLine();  in.nextLine();  in.nextLine();

        //  유틸리티 행렬을 읽는다.
        SparseMatrix u = new SparseMatrix(m, n);
        while (in.hasNext()) {
            int i = in.nextInt();       // 사용자
            int j = in.nextInt();       // 아이템
            u.put(i, j, in.nextDouble());  // 등급
        }
        in.close();
        return u;
    }

    public static void storeUtilityMatrix(SparseMatrix u, File file)
            throws FileNotFoundException {
        PrintWriter out = new PrintWriter(file);
        out.printf("%d 사용자%n", m);
        out.printf("%d 아이템%n", n);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                out.printf("%5.1f", u.get(i, j));
            }
            out.println();
        }
        out.close();
    }
    
    public static double[][] computeSimilarityMatrix(SparseMatrix u) {
        double[][] s = new double[n+1][n+1];
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k < j; k++) {
                s[j][k] = s[k][j] = cosine(u, j, k);
            }
        }
        for (int j = 1; j <= n; j++) {
        	s[j][j] = 1.0;
        }
        return s;
    }
    
    public static void computeSimilarityMatrix(SparseMatrix u, RandomAccessFile s) 
    		throws IOException {
        for (int j = 1; j <= n; j++) {
            for (int k = 1; k <= j; k++) {
                double x = cosine(u, j, k);
                s.seek((j*n + k - n - 1)*W);
                s.writeDouble(x);
                s.seek((j + k*n - n - 1)*W);
                s.writeDouble(x);
            }
        }
        for (int j = 1; j <= n; j++) {
        	s.seek((j - 1)*(n + 1)*W);
            s.writeDouble(1.0);
        }
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
    public static double cosine(SparseMatrix u, int j, int k) {
        double denominator = norm(u,j)*norm(u,k);
        return (denominator == 0 ? 0 : dot(u,j,k)/denominator);
    }
    
    /*  u[][]의 j와 k 번째 열의 내적을 반환한다.
     */
    public static double dot(SparseMatrix u, int j, int k) {
        double sum = 0.0;
        for (int i = 0; i <= m; i++) {
            sum += u.get(i, j)*u.get(i, k);
        }
        return sum;
    }
    
    /*  u[][]의 j와 k 번째 열의 노름을 반환한다.
     */
    public static double norm(SparseMatrix u, int j) {
        return Math.sqrt(dot(u,j,j));
    }
}
