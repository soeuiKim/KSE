/*  Data Analysis with Java
 *  John R. Hubbard
 *  July 12, 2017
 */

package com.example.Chapter09;

import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.Scanner;

public class Filter1 {
    private static int m;  //  사용자 수
    private static int n;  //  아이템 수

    public static void main(String[] args) {
        File purchasesFile = new File("data/Purchases1.dat");
        File utilityFile = new File("data/Utility1.dat");
        File similarityFile = new File("data/Similarity1.dat");
        try {
            int[][] u = computeUtilityMatrix(purchasesFile);
            storeUtilityMatrix(u, utilityFile);
            double[][] s = computeSimilarityMatrix(u);
            storeSimilarityMatrix(s, similarityFile);
        } catch (FileNotFoundException e) {
            System.err.println(e);
        }
    }
    
    public static int[][] computeUtilityMatrix(File file) 
            throws FileNotFoundException {
        Scanner in = new Scanner(file);
        //  다섯줄의 헤더 라인을 먼저 읽는다.
        m = in.nextInt();  in.nextLine();
        n = in.nextInt();  in.nextLine();
        in.nextLine();  in.nextLine();  in.nextLine();

        //  유틸리티 행렬을 읽는다.
        int[][] u = new int[m+1][n+1];
        while (in.hasNext()) {
            int i = in.nextInt();  // 사용자
            int j = in.nextInt();  // 아이템
            u[i][j] = 1;
        }
        in.close();
        return u;
    }

    public static void storeUtilityMatrix(int[][] u, File file)
            throws FileNotFoundException {
        PrintWriter out = new PrintWriter(file);
        out.printf("%d users%n", m);
        out.printf("%d items%n", n);
        for (int i = 1; i <= m; i++) {
            for (int j = 1; j <= n; j++) {
                out.printf("%2d", u[i][j]);
            }
            out.println();
        }
        out.close();
    }
    
    public static double[][] computeSimilarityMatrix(int[][] u) {
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

    /*  u[][]의 j번째와 k번째 열의 코사인 유사도를 반환한다.
     */
    public static double cosine(int[][] u, int j, int k) {
        double denominator = norm(u,j)*norm(u,k);
        return (denominator == 0 ? 0 : dot(u,j,k)/denominator);
    }
    
    /*  u[][]의 j번째와 k번째 열의 내적을 반환한다.
     */
    public static double dot(int[][] u, int j, int k) {
        double sum = 0.0;
        for (int i = 0; i <= m; i++) {
            sum += u[i][j]*u[i][k];
        }
        return sum;
    }
    
    /*  u[][]의 j번째 열의 노름을 반환한다.
     */
    public static double norm(int[][] u, int j) {
        return Math.sqrt(dot(u,j,j));
    }
}
