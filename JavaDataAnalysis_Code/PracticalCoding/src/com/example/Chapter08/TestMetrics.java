/*  Data Analysis with Java
 *  John R. Hubbard
 *  Jun 12, 2017
 */

package com.example.Chapter08;

import org.apache.commons.math3.ml.distance.*;

public class TestMetrics {
    public static void main(String[] args) {
        double[] x = {1, 3}, y = {5, 6};
        
        EuclideanDistance eD = new EuclideanDistance();
        System.out.printf("Euclidean distance = %.2f%n", eD.compute(x,y));
        //유클리드거리(피타고라스 정의)
        
        ManhattanDistance mD = new ManhattanDistance();
        System.out.printf("Manhattan distance = %.2f%n", mD.compute(x,y));
        //맨해튼거리_체스판거리
        
        ChebyshevDistance cD = new ChebyshevDistance();
        System.out.printf("Chebyshev distance = %.2f%n", cD.compute(x,y));
        //체비쇼프거리
        
        CanberraDistance caD = new CanberraDistance();
        System.out.printf("Canberra distance =  %.2f%n", caD.compute(x,y));
        //캔버라거리_맨해튼가중치
    }
}

/*
run:
Euclidean distance = 5.00
Manhattan distance = 7.00
Chebyshev distance = 4.00
Canberra distance =  1.00
*/
