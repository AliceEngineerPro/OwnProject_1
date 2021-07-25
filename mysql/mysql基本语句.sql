# 查看数据时间
select now() ;

# 查询mysql版本
select version() ;

# 查看所有库 show + 库名
show databases ;

# 查看库的创建信息 show create + 库名
show create database mysql ;

# 查看错误信息
show warnings ;

# 创建数据库 create database + 库名
create database learn_db ;
create database if not exists learn_db ; # 如果没有该库则创建,
create database if not exists learn_db character set utf8 ; #如果没有该库则创建, 如果有则跳过, 库编码为:utf8
# create database learn_db2;
#
# 删除数据库 drop database + 库名
# drop database learn_db2;

show create database learn_db ;
# 修改数据库信息(编码) alter database
alter database learn_db character set 'gbk' ; #编码为'gbk'
alter database learn_db character set  'utf8' ; #编码为'utf8'
show create database learn_db ;

# 使用/切换数据库 use + 库名
use learn_db ;
select database() ; # 检查当前在哪个库

# 创建数据表 create + 表名(表字段用逗分隔) + 类型[约束]
/*
    primary key-->主键
    auto_increment-->自增
    not null-->不为空
    default-->默认
    unique-->唯一
    foreign key-->外键
    comment-->注释

*/
use learn_db ;
create table people(
    id tinyint primary key auto_increment,
    name varchar(20),
    gender boolean,
    age int,
    department varchar(255),
    salary double(7,2)
) ;

create table dis_department(
    id tinyint primary key auto_increment not null ,
    department varchar(255) not null
) ;

create table test(
    id tinyint primary key auto_increment not null

) ;
# 查看建建表信息 show create + 表名
show create table people ;

# 查看表结构 desc + 表名
desc people ;

# 添加字段 alter table + 表名 add +字段名 + 类型[约束]
alter table people add is_married tinyint(1) ;
alter table people add entry_data date not null ;
alter table people add A int,add B varchar(20) ;

# 删除字段 alter table + 表名 drop +字段名
alter table people drop A ;
alter table people drop B,drop entry_data ;

# 修改字段类型 alter table + 表名 modify + 新的字段名 + 类型[约束] [修改字段的位置]
/*
    修改字段的位置:
    first-->移动到首位
    after 字段名-->移动到改字段名的后面

*/
alter table people modify gender tinyint(1) not null default 0 comment '0:保密, 1:男, 2:女' after age;

# 修改字段名 alter table + 表名 change + 原字段名 + 新字段名 + 类型[约束]
alter table people change department depart varchar(255);

# 修改表名 rename table + 愿表名 to + 新表名
rename table dis_department to people_department ;

# 删除表 drop table + 表名
drop table test ;

# 查看表结构
desc people;
select * from people
