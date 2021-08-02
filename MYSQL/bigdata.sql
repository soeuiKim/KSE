
create table tblcustomer (
    c_id    varchar(20) not null,
    c_name  varchar(10) not null,
    c_age   int,
    c_grade varchar(10) not null,
    c_jop   varchar(20),
    c_money int default 0,
    constraint pk_c_id primary key (c_id) -- 주키(primary key)설정
);

create table tblproduct (
    p_num      char(3)   NOT NULL, --제품번호
	p_name     VARCHAR(20), --제품명
	p_amount   INT, -- 재고량
	p_price    INT, -- 단가
	p_co       VARCHAR(20), --제조업체
	constraint pk_p_num primary key (p_num)
);

create table tblorder (
	o_num   CHAR(3) NOT NULL, --주문번호
	c_id    VARCHAR(20) not null, --고객아이디
	p_num   CHAR(3) not null, -- 제품번호
	o_cnt   INT, --수량
	o_area  VARCHAR(30), --배송지
	o_date  DATE, --주문날짜
	constraint pk_o_num PRIMARY KEY (o_num),
    constraint fk_c_id foreign key (c_id) references tblcustomer(c_id),
    constraint fk_p_num foreign key (p_num) references tblproduct(p_num)
);

INSERT INTO tblcustomer VALUES ('apple', '정소화', 20, 'gold', '학생', 1000);
INSERT INTO tblcustomer VALUES ('banana', '김선우', 25, 'vip', '간호사', 2500);
INSERT INTO tblcustomer VALUES ('carrot', '고명석', 28, 'gold', '교사', 4500);
INSERT INTO tblcustomer VALUES ('orange', '김용욱', 22, 'silver', '학생', 0);
INSERT INTO tblcustomer VALUES ('melon', '성원용', 35, 'gold', '회사원', 5000);
INSERT INTO tblcustomer VALUES ('peach', '오형준', NULL, 'silver', '의사', 300);
INSERT INTO tblcustomer VALUES ('pear', '채광주', 31, 'silver', '회사원', 500);

select * from tblcustomer;

INSERT INTO tblproduct VALUES ('p01', '그냥만두', 5000, 4500, '대한식품');
INSERT INTO tblproduct VALUES ('p02', '매운쫄면', 2500, 5500, '민국푸드');
INSERT INTO tblproduct VALUES ('p03', '쿵떡파이', 3600, 2600, '한빛제과');
INSERT INTO tblproduct VALUES ('p04', '맛난초콜릿', 1250, 2500, '한빛제과');
INSERT INTO tblproduct VALUES ('p05', '얼큰라면', 2200, 1200, '대한식품');
INSERT INTO tblproduct VALUES ('p06', '통통우동', 1000, 1550, '민국푸드');
INSERT INTO tblproduct VALUES ('p07', '달콤비스킷', 1650, 1500, '한빛제과');

select * from tblproduct;

INSERT INTO tblorder VALUES ('o01', 'apple', 'p03', 10, '서울시 마포구', '19/01/01');
INSERT INTO tblorder VALUES ('o02', 'melon', 'p01', 5, '인천시 계양구', '19/01/10');
INSERT INTO tblorder VALUES ('o03', 'banana', 'p06', 45, '경기도 부천시', '19/01/11');
INSERT INTO tblorder VALUES ('o04', 'carrot', 'p02', 8, '부산시 금정구', '19/02/01');
INSERT INTO tblorder VALUES ('o05', 'melon', 'p06', 36, '경기도 용인시', '19/02/20');
INSERT INTO tblorder VALUES ('o06', 'banana', 'p01', 19, '충청북도 보은군', '19/03/02');
INSERT INTO tblorder VALUES ('o07', 'apple', 'p03', 22, '서울시 영등포구', '19/03/15');
INSERT INTO tblorder VALUES ('o08', 'pear', 'p02', 50, '강원도 춘천시', '19/04/10');
INSERT INTO tblorder VALUES ('o09', 'banana', 'p04', 15, '전라남도 목포시', '19/04/11');
INSERT INTO tblorder VALUES ('o10', 'carrot', 'p03', 20, '경기도 안양시', '19/05/22');

select * from tblcustomer;
select * from tblproduct;
select * from tblorder;

select c_id, c_name, c_grade from tblcustomer;

/* 고객아이디
   고객명
   주문일자 
   조회*/
select c.c_id, c.c_name, o.o_date
    from tblcustomer c, tblorder o
    where c.c_id = o.c_id;

-- 고객아이디, 제품명, 단가, 수량 조회
select c.c_id, p.p_name, p.p_price, o.o_cnt
    from tblcustomer c, tblproduct p, tblorder o
    where c.c_id = o.c_id and p.p_num = o.p_num;
    
    --답
    select o.c_id, p.p_name, p.p_price, o.o_cnt
        from tblproduct p, tblorder o
        where p.p_num = o.p_num;
    
-- 고객아이디, 고객명, 제품명, 단가, 수량, 금액조회
select c.c_id, c.c_name, p.p_name, p.p_price, o.o_cnt, p.p_price * o.o_cnt as charge
    from tblcustomer c, tblproduct p, tblorder o
    where c.c_id = o.c_id and p.p_num = o.p_num;
    
    --답
    select c.c_id, c.c_name, p.p_name, p.p_price, o.o_cnt, p.p_price * o.o_cnt
        from tblcustomer c, tblorder o, tblproduct p
        where c.c_id = o.c_id and p.p_num = o.p_num;
    
    
-- 제품테이블의 평균 단가 이상인 제품을 구매한 고객의 고객아이디, 고객명 조회
select c.c_id, c.c_name from tblcustomer c
    where c.c_id in
    (select o.c_id from tblorder o, tblproduct p 
        where o.p_num = p.p_num and o.p_num >= avg(p_price));
        --안돼ㅠㅠ 나 서브쿼리 못하나봄
        
    --답 _단일 테이블에서 결과를 얻을수있으면 서브쿼리 아닌경우 조인
    select c_id, c_name from tblcustomer where c_id in
        (select c_id from tblorder where p_num in
            (select p_num from tblproduct where p_price >=    --단일행이니까 등호사용가능!
                (select avg(p_price) from tblproduct)));


-- 자동증가를 위해 sequence생성
create table tblboard (
    b_num int not null,
    b_subject varchar(100),
    b_contents varchar(2000),
    b_name varchar(20),
    b_date date,
    constraint pk_b_num primary key (b_num)
);

create sequence seq_b_num; --글번호 증가형 시퀀스, 1씩 증가

insert into tblboard (b_num, b_subject, b_contents, b_name, b_date)
    values (seq_b_num.nextval,'글제목','글내용','홍길동','2021-07-30');
           -- ↑오라클에서 자동증가값 설정

select * from tblboard;






/* ----------------DB설계----------
   ---------- 온라인 쇼핑몰 구현----*/

-- 고객테이블
create table tblmember (
    m_id varchar(20) not null,
    m_name varchar(20) not null,
    constraint pk_m_id primary key (m_id)
);

-- 상품테이블
create table tblgoods (
    g_code int not null,
    g_name varchar(100) not null,
    g_price int not null,
    constraint pk_g_code primary key (g_code)
);

-- 주문테이블
create table tblaccount (
    a_code int not null,       -- 영수증번호(pk)
    m_id varchar(20) not null, -- 주문고객(fk_멤버)
    a_date date not null,
    constraint pk_a_code primary key (a_code),
    constraint fK_m_id foreign key (m_id) references tblmember (m_id)
);  -- 제약조건 (pk,fk...) fk는 참조테이블 명시 ↑

create table tblsale(
    s_code int not null,
    a_code int not null,
    g_code int not null,
    s_cnt int not null,
    constraint pk_s_code primary key (s_code),
    constraint fk_a_code foreign key(a_code) references tblaccount(a_code),
    constraint fk_g_code foreign key(g_code) references tblgoods(g_code)
);


create sequence seq_g_code;
create sequence seq_a_code;
create sequence seq_s_code;

insert into tblmember(m_id, m_name) values('apple', '정소화');
insert into tblmember(m_id, m_name) values('banana', '김선우');
insert into tblmember(m_id, m_name) values('carrot', '고명석');
insert into tblmember(m_id, m_name) values('orange', '김용욱');
insert into tblmember(m_id, m_name) values('melon', '성원용');
insert into tblmember(m_id, m_name) values('peach', '오형준');
insert into tblmember(m_id, m_name) values('pear', '채광주');

select * from tblmember;

insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '이탈리안BMT', 5000);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '서브웨이클럽', 6000);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '에그마요', 4800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, 'BLT', 5500);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, 'K바베큐', 5800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '터키', 5800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '베지터블', 5800);

select * from tblgoods;

insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'apple', '2021-07-30');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'banana', '2021-07-23');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'carrot', '2021-07-30');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'orange', '2021-07-18');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'melon', '2021-07-13');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'peach', '2021-07-15');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'pear', '2021-07-11');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'apple', '2021-07-12');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'banana', '2021-07-19');
insert into tblaccount(a_code, m_id, a_date)
    values(seq_a_code.nextval, 'carrot', '2021-07-01');

select * from tblaccount;

insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 1,27,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 2,26,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 3,21,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 4,27,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 5,26,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 6,25,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 7,24,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 8,23,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 9,22,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 10,21,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 1,25,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 2,23,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 3,27,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 4,26,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 5,25,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 6,24,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 7,21,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 8,26,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 9,27,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 10,25,5);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 1,24,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 2,22,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 3,25,4);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 4,25,3);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 5,23,2);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 6,26,1);
insert into tblsale(s_code, a_code, g_code, s_cnt)
    values(seq_s_code.nextval, 10,27,2);
    
select * from tblsale;
select * from tblaccount;
select * from tblgoods;
select * from tblmember;

commit; -- 저장

-- account의 날짜정보는 7월 1일 ~ 30일 범위 내에서 추가

-- 전체주문내역을 조회, 주문코드, 주문자, 주문자id, 주문자 성명, 주문날짜 조회
select a.a_code, m.m_id, m.m_name, a.a_date
    from tblmember m, tblaccount a
    where m.m_id=a.m_id;

-- 정소화 고객의 상세 주문내용을 출력 
-- (주문자 성명, 주문코드, 상품코드, 상품명, 단가, 금액)
--select m.m_name, g.g_code, g.g_name, g.g_price 
--    from tblmember m, tblaccount a, tblsale s
--    where m.m_id = a.m_id and a.a_code = s.a_code and
--    (select m_id from tblmember where m_name='정소화');
    
    --답 (모든테이블 조인)
    select m.m_name, g.g_code, g.g_name, a.a_code, g.g_price, s.s_cnt, s.s_cnt * g.g_price 
        from tblmember m, tblgoods g, tblaccount a, tblsale s
        where m.m_id = a.m_id and a.a_code = s.a_code and g.g_code = s.g_code
            and m.m_name = '정소화';
    
-- 가장 최근에 주문한 주문코드에 대하여 주문상세내역을 출력
-- (주문코드, 제품명, 단가, 수량, 금액) 

--select a.a_code, g.g_name, g.g_price, s.s_cnt, g.g_price * s.s_cnt
--    from tblgoods g, tblaccount a, tblsale s
--    where a.a_code = s.a_code and g.g_code = s.g_code 
--        and (select max(a_code) from tblaccount) ;

select s.a_code, g.g_name, g.g_price, s.s_cnt, g.g_price * s.s_cnt
    from tblsale s, tblgoods g
    where s.a_code = g.g_code 
    and s.a_code = (select max(a_code) from tblaccount);

    





