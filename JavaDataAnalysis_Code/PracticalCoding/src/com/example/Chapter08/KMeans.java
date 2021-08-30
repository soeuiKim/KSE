package com.example.Chapter08;

import java.util.HashSet;
import java.util.Random;
import java.util.Set;

public class KMeans {
    private static final double[][] DATA = {{1,1}, {1,3}, {1,5}, {2,6}, {3,2}, 
        {3,4}, {4,3}, {5,6}, {6,3}, {6,4}, {7,1}, {7,5}, {7,6}};
    private static final int M = DATA.length;  
    private static final int K = 3;  
    private static HashSet<Point> points;  
    private static HashSet<Cluster> clusters = new HashSet();
    private static Random RANDOM = new Random();
    
    public static void main(String[] args) {
        points = load(DATA);
        
        //임의의 포인트 p를 선택한다.
        int i0 = RANDOM.nextInt(M);
        Point p = new Point(DATA[i0][0], DATA[i0][1]);
        points.remove(p);
        
        //p를 포함하는 단일 데이터 셋 생성
        HashSet<Point> initSet = new HashSet();
        initSet.add(p);
        
        //k-1 데이터 포인트를 initSet에 추가
        for (int i = 0; i < K; i++) {
        	p = farthestFrom(initSet);
        	initSet.add(p);
        	points.remove(p);
        }
        
        // initSet에서 각 포인트에 대한 클러스터를 생성
        for (Point point : initSet) {
        	Cluster cluster = new Cluster(point);
        	clusters.add(cluster);
        }
        
        //남은 각 포인트를 가장 가까운 클러스터에 업데이트
        for (Point point : points) {
        	Cluster cluster = closestTo(point);
        	cluster.add(point);;
        	cluster.recomputeCentroid();
        }
        System.out.println(clusters);
    } 
    
    //특정포인트와 가장가까운 중심에이 있는 클러스터 반환
    private static Cluster closestTo(Point point) {
    	double minDist = Double.POSITIVE_INFINITY;
    	Cluster c =null;
    	for ( Cluster cluster : clusters) {
    		double d = distance2(cluster.getCentroid(), point);
    		if( d < minDist) {
    			minDist= d;
    			c = cluster;
    			}
    		} return c;
    	}
    //특정셋과 가장 멀리 떨어진 포인트를 반환한다.
    private static Point farthestFrom(Set<Point> set) {
    	Point p =null;
    	double maxDist = 0.0;
    	for (Point point : points) {
    		if (set.contains(point)) {
    			continue;
    		}
    		double d = dist(point, set);
    		if ( d> maxDist) {
    			p = point;
    			maxDist = d;
    		}
    	} 
    	return p;
    }
    
    // 에디터 셋 에서 p와 가장 가까이 있는 포인트와의 거리를 반환한다.
    public static double dist(Point p, Set<Point> set) {
    	double minDist = Double.POSITIVE_INFINITY;
    	for (Point point : set) {
    		double d = distance2(p, point);
    		minDist = (d < minDist ? d : minDist);
    	}
    	return minDist;
    }
    
    // 두 지점간의 유클리디안 거리의 제곱을 구한다.
    public static double distance2(Point p, Point q) {
    	double dx = p.getX() - q.getX();
    	double dy = p.getY() - q.getY();
    	return dx*dx + dy*dy;
    }
    
    private static HashSet<Point> load(double[][] data) {
    	HashSet<Point> points = new HashSet();
    	for (double[] datum : DATA) {
    		points.add(new Point(datum[0], datum[1]));
    	}
    	return points;
    }
    
    
}//end of class
/*
run:
[[1.0, 1.0], [1.0, 3.0], [1.0, 5.0], [2.0, 6.0], [3.0, 2.0], [3.0, 4.0], [4.0, 3.0]]
[[5.0, 6.0], [6.0, 3.0], [6.0, 4.0], [7.0, 5.0], [7.0, 6.0]]
[[7.0, 1.0]]
run:
[[5.0, 6.0], [6.0, 3.0], [6.0, 4.0], [7.0, 1.0], [7.0, 5.0], [7.0, 6.0]]
[[1.0, 1.0], [1.0, 3.0], [3.0, 2.0], [3.0, 4.0], [4.0, 3.0]]
[[1.0, 5.0], [2.0, 6.0]]
*/
