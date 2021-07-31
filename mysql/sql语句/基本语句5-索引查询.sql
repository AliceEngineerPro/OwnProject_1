-- 索引语法
# 创建索引
create table tb_1(
    id int primary key comment 'ID' auto_increment ,
    name varchar(20) ,
    salary int default 3000
) ;

insert into tb_1(name) values ('111'),
                              ('222'),
                              ('333'),
                              ('444') ;

drop table tb_1 ;

alter table tb_1 drop salary ;
select * from tb_1 ;

delimiter !!
create procedure autoinsert()
begin
    declare i int default 1;
    while (i<500000)do
        insert into tb_1 value (i,'段博') ;
        set i=i+1 ;
        end while ;
end !!

delimiter ;
call autoinsert() ;

select * from tb_1 where id = 48999 ;

alter table tb_1 add index (id) ;

desc tb_1 ;
show create table tb_1 ;

# drop index id on tb_1 ;

drop table tb_1 ;

