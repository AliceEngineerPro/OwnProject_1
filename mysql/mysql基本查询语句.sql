create table dis_exam(
    id int primary key auto_increment not null ,
    student_name varchar(20) not null ,
    exam_python double default 0 ,
    exam_linux double default 0 ,
    exam_mysql double default 0
);

insert into dis_exam values (1,'1号', 98, 98, 98),
                            (2,'2号',35, 98, 67),
                            (3,'3号',59, 59, 62),
                            (4,'4号', 88, 89, 82),
                            (5,'5号', 88, 98, 67),
                            (6,'6号', 86, 100, 55);

insert into dis_exam(student_name) values ('1号'), ('2号'), ('1号');

use learn_db;

# 查询所有 select * from + 表名
select * from dis_exam ;

# 去重 select distinct + 字段名 from 表名
select distinct student_name from dis_exam ;

# 查询一到多个字段的值 select 字段名1,字段名2,...,字段名n form + 表名
select student_name from dis_exam ;
select id, student_name from dis_exam ;

# 查询时显示(临时更改, 一般用于数值型数据)
select student_name, exam_linux from dis_exam ;
select student_name, exam_linux+10 from dis_exam ;

# 查询临时显示表头(别名) select +字段名 as + 别名 from 表名
select student_name as name from dis_exam ;

# 条件判断
/*
    比较运算符: > < >= <= <> !=
        between x and y -->在x到y之间
        in(x, y, z) -->值是x或y或z
        line '张三%' --> 等于..., %表示通配符, %->表示任意多的字符; _->表示一个字符
    逻辑运算符: and or not

    is null -->查询空值

*/
select * from dis_exam where exam_linux>60 ;
select * from dis_exam where exam_python!=88 ;
select * from dis_exam where exam_mysql between 80 and 100 ;
select * from dis_exam where exam_python in (88, 98) ;
select * from dis_exam where student_name like '1%' ;
