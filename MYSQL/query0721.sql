use mysql;

CREATE TABLE 고객 (
	고객아이디   VARCHAR(20)	 NOT NULL, # not null은 비어있을수 없음.
	고객이름    VARCHAR(10)	 NOT NULL,
	나이	      INT,
	등급	      VARCHAR(10)	 NOT NULL,
	직업	      VARCHAR(20),
	적립금	  INT   DEFAULT 0,
	PRIMARY KEY(고객아이디)
); 

# 오타 및 수정사항 체크(실행해볼것)
# 이럴때는 삭제하고 다시만들것

CREATE TABLE  제품 (
	제품번호   CHAR(3)   NOT NULL, # 제품번호는 p숫자2자리입니다._빈자리가 없어서 고정형 데이터
	제품명     VARCHAR(20), # 최대값 20에 가변적인 데이터
	재고량     INT,
	단가       INT,
	제조업체    VARCHAR(20),
	PRIMARY KEY(제품번호), # primary는 공백,중복 x
	CHECK (재고량 >= 0 AND 재고량 <=10000) # 수량 제약을 거는것.
);

-- 주석 # 주석 
/* 여러줄주석이야요 
하하하하하하하 */

CREATE TABLE  주문 (
	주문번호   CHAR(3)    NOT NULL,
	주문고객   VARCHAR(20),
	주문제품   CHAR(3),
	수량      INT,
	배송지    VARCHAR(30),
	주문일자   DATE,
	PRIMARY KEY(주문번호),   #references 테이블 참조
	FOREIGN KEY(주문고객)   REFERENCES   고객(고객아이디),
	FOREIGN KEY(주문제품)   REFERENCES   제품(제품번호)
    # foreign 다른 테이블에서 가져올수 있는 키
);




INSERT INTO 고객 VALUES ('apple', '정소화', 20, 'gold', '학생', 1000);
INSERT INTO 고객 VALUES ('banana', '김선우', 25, 'vip', '간호사', 2500);
INSERT INTO 고객 VALUES ('carrot', '고명석', 28, 'gold', '교사', 4500);
INSERT INTO 고객 VALUES ('orange', '김용욱', 22, 'silver', '학생', 0);
INSERT INTO 고객 VALUES ('melon', '성원용', 35, 'gold', '회사원', 5000);
INSERT INTO 고객 VALUES ('peach', '오형준', NULL, 'silver', '의사', 300);
INSERT INTO 고객 VALUES ('pear', '채광주', 31, 'silver', '회사원', 500);

select 고객아이디, 고객이름, 등급 from 고객;

select * from 고객;
#   * 는 ALL(모두) 이라는 뜻. 설계시 작성한 속성의 순서대로 검색

INSERT INTO 제품 VALUES ('p01', '그냥만두', 5000, 4500, '대한식품');
INSERT INTO 제품 VALUES ('p02', '매운쫄면', 2500, 5500, '민국푸드');
INSERT INTO 제품 VALUES ('p03', '쿵떡파이', 3600, 2600, '한빛제과');
INSERT INTO 제품 VALUES ('p04', '맛난초콜릿', 1250, 2500, '한빛제과');
INSERT INTO 제품 VALUES ('p05', '얼큰라면', 2200, 1200, '대한식품');
INSERT INTO 제품 VALUES ('p06', '통통우동', 1000, 1550, '민국푸드');
INSERT INTO 제품 VALUES ('p07', '달콤비스킷', 1650, 1500, '한빛제과');

select * from 제품;

INSERT INTO 주문 VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '19/01/01');
INSERT INTO 주문 VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '19/01/10');
INSERT INTO 주문 VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '19/01/11');
INSERT INTO 주문 VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '19/02/01');
INSERT INTO 주문 VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '19/02/20');
INSERT INTO 주문 VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '19/03/02');
INSERT INTO 주문 VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '19/03/15');
INSERT INTO 주문 VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '19/04/10');
INSERT INTO 주문 VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '19/04/11');
INSERT INTO 주문 VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '19/05/22');

select * from 주문;

select 제조업체 from 제품;

# 실행된것을 재실행하면 중복이 되므로 에러가 된다.
# 주문ㅌㅔ이블에서 고객아이디와 제품번호는 중복이가능하지만 주문번호는 프라이머리 키 이므로 중복x

# select에서 중복을 걸러내는 명령어 distinct
select distinct 제조업체 from 제품;


select 제품명, 단가 as 금액 from 제품;
# as는 출력시에만 속성명을 변경하여 보여준다.(원래 설계한 속성명은 바뀌지 않는다.)

select 제품명, 단가, 단가 + 500 as "조정 단가" from 제품;
   # 띄어쓰기할때는 '," 사용 ( 속석명은 되도록 띄어씌기 x )

-- 30% 할인된 단가를 할인단가로 출력 (기존 단가도 출력)
select 제품명, 단가, 단가 * 0.7  as 할인단가 from 제품;
			    # 단가 * (1- 0.3)

select 제품명, 재고량, 단가, 제조업체 from 제품  # 줄바꿈 가능 _ 명령어를 끊어 쓰면 x
	where 제조업체 = '한빛제과';  # 문자열이므로 ' 사용 (숫자일 경우 그냥 입력)

-- 주문테이블에서 apple고객이 15이상 주문한 주문제품, 수량, 주문일자 검색(예제 7-19)
select 주문제품, 수량, 주문일자, 주문고객 from 주문
	where 주문고객 = 'apple' and 수량 >= 15; # 숫자는 '' 사용x
    # '' 안에는 대소문자 구분할것.

-- 주문테이블에서 apple고객이 주문했거나 15개이상 주문된 제품의 주문제품 수량 주문일자 주문고객 검색
select 주문고객, 주문제품, 수량, 주문일자 from 주문 
	where 주문고객 = 'apple'  or  수량 >= 15;

-- 제품테이블에서 단가가 2000원이상이면서 3000원이하인 제품의 제품명 단가 제조업체 검색
select 제품명, 단가, 제조업체 from 제품
	where 단가 >= 2000 and 단가 <= 3000; #같은 속성명을 사용하더라도 입력해줘야함_생략불가
    # and ,or 은 완성된 문장을 이어주는것이기 때문에 속성명 생략을 할 수 없다.

select * from 제품 where 단가 >=2000 and 단가<=3000;

-- 김씨 성을 가진 고객 조회
select * from 고객;  # 고객테이블 확인
select * from 고객 where 고객이름 like '김%';
        # '김'으로 입력하면 문법적으로 문제는 없지만 검색이 되지 않는다.


# select구문은 출력물에 영향을 주는 것이므로 속성은 변하지않는다.(속성변경을 insert 사용)

-- 고객이름 등급 나이검색, 나이를 기준으로 내림차순 정렬
select * from 고객 order by 나이 desc; # 비어있는 값은 제일 아래로 온다
	# asc 오름차순(기본)  /  desc 내림차순

-- 주문테이블에서 수량이 10개 이상인 주문의 주문고객 주문제품 수량 주문일자 검색
-- 단, 주문제품을 기준으로 오름차순 정렬, 동일제품은 수량을 기준으로 내림차순 정렬
select 주문고객, 주문제품, 수량, 주문일자 from 주문
	where 수량 >= 10 order by 주문제품 asc, 수량 desc;

-- 제품단가의 평균 구하기.
select avg(단가) as 단가평균 from 제품 ;

-- 고객이 몇 명인지 검색
select count(고객아이디) as 고객수 from 고객; # 프라이머리키가 설정된 속성을 카운트하는게 오류x
select count(나이) as 고객수 from 고객; # null은 카운트 되지 않는다.

-- 집계함수_ㅈㅔ품테이블에서 제조업체의 수 검색
select count(제조업체) from 제품; # 중복포함하여 값이 나옴.
select count(distinct(제조업체)) from 제품;

-- 주문테이블에서 주문제품별 수량의 합계를 검색
select * from 주문;
select 주문제품, sum(수량) as 부분합 from 주문 group by 주문제품;
 # 그룹바이한 속성만 출력해야함, 다른 속성이 오면 정확한 값이 되지않음.

-- 제품테이블에서 제조업체별로 제조한 제품의 개수와 제품 중 가장 비싼 단가를 검색
-- 제품의 개수는 제품수로 출력하고 비싼 단가는 최고가로 출력
select 제조업체, count(*) as 제품수, max(단가) as 최고가
	from 제품 group by 제조업체;

-- 제조업체별 제품개수와 재고량의 최대값을 출력
select 제조업체, count(제조업체), max(재고량) from 제품 group by 제조업체;

-- 제조업체별 제품개수와 재고량의 최대값을 출력, 제품개수가 3개 이상인 경우 조회
select 제조업체, count(*), max(재고량) from 제품 
	group by 제조업체 having count(*) >= 3;
# having 구문은 group by 구문에 의해 처리된 결과를 대상으로 함

select * from 고객;
-- 고객테이블에서 등급별 평균 출력, 적립금 평균 출력
select 등급, avg(적립금) from 고객 group by 등급 
	having avg(적립금) >= 1000;
# 그룹바이했을대는 단독출력x, 직계 함수를 이용한것만 출력가능











