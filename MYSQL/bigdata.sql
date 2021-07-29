
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


    





