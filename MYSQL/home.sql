use mysql;

--  DDL문
--   : 데이터를 정의하는 언어(오브젝드 정의)
--  스키마 : 하나의 데이터베이스
--  도메인 : 속성의 테이터 타입과 크기, 제약조건등을 지정한 정보(속성정보)
--  테이블 : 데이터 저장공간
--  뷰 : 가상의 논리 테이블 ( 창문 )
--  인덱스 : 검색을 빠르게 하기위한 데이터 구조
--  
--  구문
--  
--  생성 : create 
--  변경 : alter
--  삭제 : drop _삭제
-- 	      truncate _내용삭제

create table cu (
	c_id varchar(20) not null,
    c_name varchar(20) not null,
    c_age int not null,
    c_grade varchar(20),
    c_jop varchar(20),
    c_point int default 0,
    primary key (c_id)
    );

insert into cu values('apple', '정소화', 20, 'gold', '학생', 1000);
insert into cu values('banana', '김선우', 25, 'vip', '간호사', 2500);
insert into cu values('carrot', '고명석', 28, 'gold', '교사', 4500);
insert into cu values('orange', '김용욱', 22, 'silver', '학생', 0);
insert into cu values('melon', '성원용', 35, 'gold', '회사원', 5000);
insert into cu values('peach', '오형준', 26, 'silver', '의사', 300);
insert into cu values('pear', '채광주', 31, 'silver', '회사원', 500);

create table gd (
	g_num char(3) not null,
    g_name varchar(20) not null,
    g_amount int, 
    g_price int,
    g_com varchar(20),
    primary key (g_num)
);

select * from gd;
show tables;

insert into gd values ('p01', '그냥만두', 5000, 4500, '대한식품');
insert into gd values ('p02', '매운쫄면', 2500, 5500, '민국푸드');
insert into gd values ('p03', '쿵떡파이', 3600, 2600, '한빛제과');
insert into gd values ('p04', '맛난초콜릿', 1250, 2500, '한빛제과');
insert into gd values ('p05', '얼큰라면', 2200, 1200, '대한식품');
insert into gd values ('p06', '통통우동', 1000, 1550, '민국푸드');
insert into gd values ('p07', '달콤비스킷', 1650, 1500, '한빛제과');

select * from gd;

create table od (
	o_num char(3) not null,
    c_id varchar(20) not null,
    g_num char(3) not null,
    o_cnt int,
    o_adr varchar(30),
    o_date date,
    primary key (o_num),
    foreign key (c_id) references cu(c_id),
    foreign key (g_num) references gd(g_num)
    );
    
insert into od values ('o01', 'apple', 'p03', 10, '서울시 마포구', '19/01/01');
insert into od values ('o02', 'melon', 'p01', 5, '인천시 계양구', '19/01/10');
INSERT INTO od values ('o03', 'banana', 'p06', 45, '경기도 부천시', '19/01/11');
INSERT INTO od VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '19/02/01');
INSERT INTO od VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '19/02/20');
INSERT INTO od VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '19/03/02');
INSERT INTO od VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '19/03/15');
INSERT INTO od VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '19/04/10');
INSERT INTO od VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '19/04/11');
INSERT INTO od VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '19/05/22');

select * from od;

-- alter구문 
-- 	테이블 구조 변경
-- 	alter table 테이블명 change 바꿀이름 바꿀속성;
--     칼럼 추가 삭제
--     alter table 테이블명 add 칼럼명 자료형; -칼럼추가(맨뒤에)
--     alter table 테이블명 add 새컬럼명 자료형 first; -맨앞에
--     alter table 테이블명 add 새컬럼명 자료형 after 앞컬럼명 -지정칼럼뒤에
--     alter table 테이블명 drop 컬럼명; -삭제
--     alter table 테이블명 add foreign key 외래키명 references 테이블명(외래키명); -외래키삽입
--     alter table 테이블명 drop foreign key; -외래키 삭제
--     ...등등 다양하게 삽입 및 삭제 가능

--  DML활용_ 테이블에대한 테이터 삽입, 수정, 삭제, 조회 명령문
-- 데이터 생성 insert
-- 데이터 조회 select
-- 데이터 변경 update
-- 데이터 삭제 delete

-- insert 구문
-- 	insert into 테이블명 (칼럼1, 칼럼2, ..)values(값1,값2, ..); 
--  insert into 테이블명 values (값1,값2, ..);

-- select 구문
-- 	select [옵션] 칼럼명 from 테이블명 where...;
-- 		all = * -> 중복을 포함한 모든값 조회
-- 		distinct -> 중복을 제거한 조회 
-- 		as 를 이용하여 별명을 부여할 수 있다. 

-- update 구문
--  update 테이블명 set 칼럼명 = 값1, 칼럼명 = 값2, ... where...;

-- delete 구문
-- 	delete from 테이블명 where ...; - where가 없으면 테이블 모두 삭제

-- DCL문
-- 사용자 권한 = 접근통제 = 사용자를 등록하고, 사용자에게 특정 데이터 베이스를 사용할 수 있는 권리를 부여하는 작업
-- 트랜잭션 = 안전한 거래보장 = 동시에 다수의 작업을 독립적으로 안전하게 처리하기 위한 상호 작용 단위
--  트랜잭션에는 TCL문이 있다
-- TCL과 DCL은 대상이 달라 별개의 개념으로 분류하지만 제어기능의 공통점으로 DCL의 일부로 분류하기도 한다

-- DCL
-- grant 사용자 권한부여
-- revoke 사용자 권한회수

-- TCL
-- commit 트랜잭션 확정
-- rollback 트랜잭션 취소
-- checkpoint 복귀지점 설정


create table employee ( 
	em_id int not null auto_increment, 
    em_name char(50) not null,   
    em_rank char(50) not null,          
    em_pay int not null,               
    primary key(em_id)
);
    
insert into employee (em_name,em_rank,em_pay)
	values ('홍길동','과장',1000000);
    
select * from employee;

update employee set em_pay = 1000000 where em_name = '홍길동';

create view pay
	as select em_name from employee where em_pay = 3000000;

select * from pay;
    
    

    
    
    
    
    
    
    