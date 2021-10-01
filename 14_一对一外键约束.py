''
'''
设计数据库中的表 - ER图（实体关系图） - 概念模型图

(图书管理)读者，图书       多对多关系  ##需要建立中间表
(商城)用户，购物车，商品，订单        用户对购物车，一对一；用户对订单，一对多；商品对订单，多对多    
(共享单车)用户，单车     多对多
(ID身份)人，身份证     一对一

 #尽量以业务无关的列当主键，它可以唯一的标识一条记录
create table tb_person
(
pid int auto_increment,
pname varchar(50),
primary key(pid)
);

create table tb_idcard
(
cid int auto_increment,
cno char(18) not null,      #char 定长字符串
ps varchar(255) not null,
expire date not null,
pid int not null,
primary key (cid)
);

一对一外键关联： #在多对一的基础上加上一个唯一约束
alter table tb_idcard add constraint fk_card_pid foreign key (pid)
references tb_person (pid);

alter table tb_idcard add constraint uni_card_pid unique (pid);

#人的身份证也要加上唯一性约束
alter table tb_idcard add constraint uni_card_cno unique (cno);
'''










