
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


    





