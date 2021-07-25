use learn_db;

# 排序查询
/*
    select + 字段名/*(多个字段名用逗号隔开) from + 表名 order by + 要排序的字段名
        order by + 字段名 [asc | desc]
        order by 默认为升序
        order by + 字段名 desc -->倒序
 */

select student_name, exam_python from dis_exam order by exam_python ;
select student_name, exam_python from dis_exam order by exam_python desc ;

select student_name, exam_python+exam_mysql+exam_linux as sum from dis_exam order by sum desc ;

# 分组查询 select + 字段名/(*) from 表名 group by + 按哪个字段分类
select student_name from dis_exam group by student_name ;

# 分组后条件筛选用having select + 字段名/(*) from 表名 group by + 按哪个字段分类 having [条件]
select student_name , sum(exam_mysql) from dis_exam group by student_name having sum(exam_mysql)>100 ;

# 计数查询 select count(字段名/(*)) from 表名 [条件]
select count(*) from dis_exam ;

# 平均值查询 select avg(字段名) from + 表名
select sum(exam_mysql)/count(student_name) from dis_exam ;
select avg(exam_mysql) from dis_exam ;

# 最值
# 最大值 select max(字段名/(*)) from + 表名
select max(exam_mysql) from dis_exam ;
select max(exam_mysql+exam_linux+exam_python) from dis_exam ;
#最小值 select min(字段名/(*)) from + 表名
select min(exam_mysql) from dis_exam ;
select min(exam_mysql+exam_linux+exam_python) from dis_exam ;

# 查看表中的前x行 select * from + 表名 limit x
select * from dis_exam limit 3 ;
# 查看跳过x行显示y行 select * from + 表名 limit x,y
select * from dis_exam limit 2,1 ;
