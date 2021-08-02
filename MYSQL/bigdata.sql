
create table tblcustomer (
    c_id    varchar(20) not null,
    c_name  varchar(10) not null,
    c_age   int,
    c_grade varchar(10) not null,
    c_jop   varchar(20),
    c_money int default 0,
    constraint pk_c_id primary key (c_id) -- ��Ű(primary key)����
);

create table tblproduct (
    p_num      char(3)   NOT NULL, --��ǰ��ȣ
	p_name     VARCHAR(20), --��ǰ��
	p_amount   INT, -- ���
	p_price    INT, -- �ܰ�
	p_co       VARCHAR(20), --������ü
	constraint pk_p_num primary key (p_num)
);

create table tblorder (
	o_num   CHAR(3) NOT NULL, --�ֹ���ȣ
	c_id    VARCHAR(20) not null, --�����̵�
	p_num   CHAR(3) not null, -- ��ǰ��ȣ
	o_cnt   INT, --����
	o_area  VARCHAR(30), --�����
	o_date  DATE, --�ֹ���¥
	constraint pk_o_num PRIMARY KEY (o_num),
    constraint fk_c_id foreign key (c_id) references tblcustomer(c_id),
    constraint fk_p_num foreign key (p_num) references tblproduct(p_num)
);

INSERT INTO tblcustomer VALUES ('apple', '����ȭ', 20, 'gold', '�л�', 1000);
INSERT INTO tblcustomer VALUES ('banana', '�輱��', 25, 'vip', '��ȣ��', 2500);
INSERT INTO tblcustomer VALUES ('carrot', '���', 28, 'gold', '����', 4500);
INSERT INTO tblcustomer VALUES ('orange', '����', 22, 'silver', '�л�', 0);
INSERT INTO tblcustomer VALUES ('melon', '������', 35, 'gold', 'ȸ���', 5000);
INSERT INTO tblcustomer VALUES ('peach', '������', NULL, 'silver', '�ǻ�', 300);
INSERT INTO tblcustomer VALUES ('pear', 'ä����', 31, 'silver', 'ȸ���', 500);

select * from tblcustomer;

INSERT INTO tblproduct VALUES ('p01', '�׳ɸ���', 5000, 4500, '���ѽ�ǰ');
INSERT INTO tblproduct VALUES ('p02', '�ſ��̸�', 2500, 5500, '�α�Ǫ��');
INSERT INTO tblproduct VALUES ('p03', '��������', 3600, 2600, '�Ѻ�����');
INSERT INTO tblproduct VALUES ('p04', '�������ݸ�', 1250, 2500, '�Ѻ�����');
INSERT INTO tblproduct VALUES ('p05', '��ū���', 2200, 1200, '���ѽ�ǰ');
INSERT INTO tblproduct VALUES ('p06', '����쵿', 1000, 1550, '�α�Ǫ��');
INSERT INTO tblproduct VALUES ('p07', '���޺�Ŷ', 1650, 1500, '�Ѻ�����');

select * from tblproduct;

INSERT INTO tblorder VALUES ('o01', 'apple', 'p03', 10, '����� ������', '19/01/01');
INSERT INTO tblorder VALUES ('o02', 'melon', 'p01', 5, '��õ�� ��籸', '19/01/10');
INSERT INTO tblorder VALUES ('o03', 'banana', 'p06', 45, '��⵵ ��õ��', '19/01/11');
INSERT INTO tblorder VALUES ('o04', 'carrot', 'p02', 8, '�λ�� ������', '19/02/01');
INSERT INTO tblorder VALUES ('o05', 'melon', 'p06', 36, '��⵵ ���ν�', '19/02/20');
INSERT INTO tblorder VALUES ('o06', 'banana', 'p01', 19, '��û�ϵ� ������', '19/03/02');
INSERT INTO tblorder VALUES ('o07', 'apple', 'p03', 22, '����� ��������', '19/03/15');
INSERT INTO tblorder VALUES ('o08', 'pear', 'p02', 50, '������ ��õ��', '19/04/10');
INSERT INTO tblorder VALUES ('o09', 'banana', 'p04', 15, '���󳲵� ������', '19/04/11');
INSERT INTO tblorder VALUES ('o10', 'carrot', 'p03', 20, '��⵵ �Ⱦ��', '19/05/22');

select * from tblcustomer;
select * from tblproduct;
select * from tblorder;

select c_id, c_name, c_grade from tblcustomer;

/* �����̵�
   ����
   �ֹ����� 
   ��ȸ*/
select c.c_id, c.c_name, o.o_date
    from tblcustomer c, tblorder o
    where c.c_id = o.c_id;

-- �����̵�, ��ǰ��, �ܰ�, ���� ��ȸ
select c.c_id, p.p_name, p.p_price, o.o_cnt
    from tblcustomer c, tblproduct p, tblorder o
    where c.c_id = o.c_id and p.p_num = o.p_num;
    
    --��
    select o.c_id, p.p_name, p.p_price, o.o_cnt
        from tblproduct p, tblorder o
        where p.p_num = o.p_num;
    
-- �����̵�, ����, ��ǰ��, �ܰ�, ����, �ݾ���ȸ
select c.c_id, c.c_name, p.p_name, p.p_price, o.o_cnt, p.p_price * o.o_cnt as charge
    from tblcustomer c, tblproduct p, tblorder o
    where c.c_id = o.c_id and p.p_num = o.p_num;
    
    --��
    select c.c_id, c.c_name, p.p_name, p.p_price, o.o_cnt, p.p_price * o.o_cnt
        from tblcustomer c, tblorder o, tblproduct p
        where c.c_id = o.c_id and p.p_num = o.p_num;
    
    
-- ��ǰ���̺��� ��� �ܰ� �̻��� ��ǰ�� ������ ���� �����̵�, ���� ��ȸ
select c.c_id, c.c_name from tblcustomer c
    where c.c_id in
    (select o.c_id from tblorder o, tblproduct p 
        where o.p_num = p.p_num and o.p_num >= avg(p_price));
        --�ȵŤФ� �� �������� ���ϳ���
        
    --�� _���� ���̺��� ����� ������������ �������� �ƴѰ�� ����
    select c_id, c_name from tblcustomer where c_id in
        (select c_id from tblorder where p_num in
            (select p_num from tblproduct where p_price >=    --�������̴ϱ� ��ȣ��밡��!
                (select avg(p_price) from tblproduct)));


-- �ڵ������� ���� sequence����
create table tblboard (
    b_num int not null,
    b_subject varchar(100),
    b_contents varchar(2000),
    b_name varchar(20),
    b_date date,
    constraint pk_b_num primary key (b_num)
);

create sequence seq_b_num; --�۹�ȣ ������ ������, 1�� ����

insert into tblboard (b_num, b_subject, b_contents, b_name, b_date)
    values (seq_b_num.nextval,'������','�۳���','ȫ�浿','2021-07-30');
           -- �����Ŭ���� �ڵ������� ����

select * from tblboard;






/* ----------------DB����----------
   ---------- �¶��� ���θ� ����----*/

-- �����̺�
create table tblmember (
    m_id varchar(20) not null,
    m_name varchar(20) not null,
    constraint pk_m_id primary key (m_id)
);

-- ��ǰ���̺�
create table tblgoods (
    g_code int not null,
    g_name varchar(100) not null,
    g_price int not null,
    constraint pk_g_code primary key (g_code)
);

-- �ֹ����̺�
create table tblaccount (
    a_code int not null,       -- ��������ȣ(pk)
    m_id varchar(20) not null, -- �ֹ���(fk_���)
    a_date date not null,
    constraint pk_a_code primary key (a_code),
    constraint fK_m_id foreign key (m_id) references tblmember (m_id)
);  -- �������� (pk,fk...) fk�� �������̺� ��� ��

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

insert into tblmember(m_id, m_name) values('apple', '����ȭ');
insert into tblmember(m_id, m_name) values('banana', '�輱��');
insert into tblmember(m_id, m_name) values('carrot', '���');
insert into tblmember(m_id, m_name) values('orange', '����');
insert into tblmember(m_id, m_name) values('melon', '������');
insert into tblmember(m_id, m_name) values('peach', '������');
insert into tblmember(m_id, m_name) values('pear', 'ä����');

select * from tblmember;

insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '��Ż����BMT', 5000);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '�������Ŭ��', 6000);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '���׸���', 4800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, 'BLT', 5500);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, 'K�ٺ�ť', 5800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '��Ű', 5800);
insert into tblgoods(g_code, g_name, g_price) 
    values(seq_g_code.nextval, '�����ͺ�', 5800);

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

commit; -- ����

-- account�� ��¥������ 7�� 1�� ~ 30�� ���� ������ �߰�

-- ��ü�ֹ������� ��ȸ, �ֹ��ڵ�, �ֹ���, �ֹ���id, �ֹ��� ����, �ֹ���¥ ��ȸ
select a.a_code, m.m_id, m.m_name, a.a_date
    from tblmember m, tblaccount a
    where m.m_id=a.m_id;

-- ����ȭ ���� �� �ֹ������� ��� 
-- (�ֹ��� ����, �ֹ��ڵ�, ��ǰ�ڵ�, ��ǰ��, �ܰ�, �ݾ�)
--select m.m_name, g.g_code, g.g_name, g.g_price 
--    from tblmember m, tblaccount a, tblsale s
--    where m.m_id = a.m_id and a.a_code = s.a_code and
--    (select m_id from tblmember where m_name='����ȭ');
    
    --�� (������̺� ����)
    select m.m_name, g.g_code, g.g_name, a.a_code, g.g_price, s.s_cnt, s.s_cnt * g.g_price 
        from tblmember m, tblgoods g, tblaccount a, tblsale s
        where m.m_id = a.m_id and a.a_code = s.a_code and g.g_code = s.g_code
            and m.m_name = '����ȭ';
    
-- ���� �ֱٿ� �ֹ��� �ֹ��ڵ忡 ���Ͽ� �ֹ��󼼳����� ���
-- (�ֹ��ڵ�, ��ǰ��, �ܰ�, ����, �ݾ�) 

--select a.a_code, g.g_name, g.g_price, s.s_cnt, g.g_price * s.s_cnt
--    from tblgoods g, tblaccount a, tblsale s
--    where a.a_code = s.a_code and g.g_code = s.g_code 
--        and (select max(a_code) from tblaccount) ;

select s.a_code, g.g_name, g.g_price, s.s_cnt, g.g_price * s.s_cnt
    from tblsale s, tblgoods g
    where s.a_code = g.g_code 
    and s.a_code = (select max(a_code) from tblaccount);

    





