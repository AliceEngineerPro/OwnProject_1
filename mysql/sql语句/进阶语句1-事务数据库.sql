use learn_db ;

create table acc(
    id int primary key auto_increment comment 'ID' ,
    name varchar(20) comment '姓名' ,
    money int comment '金额'
) ;

insert into acc(name, money) values('村长',8000),
                                    ('政委',8000) ;

select * from acc ;

# 事务
start transaction ;  # 开始事务
update acc set money=money-5000 where id=1 ;
rollback ;  # 回滚事务
update acc set money=money-5000 where id=1 ;
update acc set money=money+5000 where id=2 ;
commit ;  # 提交事务
