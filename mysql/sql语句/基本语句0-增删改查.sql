use learn_db ;

# 查询所有字段已经信息 select * from + 表名
select * from people ;

# 增
# 添加数据
/*
    insert into + 表名(要增加的字段名) values(对应字段的数据)
    insert into + 表名 values(全部字段对应的值)
    insert into + 表名 set
*/
insert into people(id, name, age, gender, department, salary, is_married) values(2, 'alex', 18, 1, '技术部门', 5000, 1) ;
insert into people(name, age, department, salary) values ('张三', 38, '技术部门', 500.5) ;
insert into people(name, age, department, salary) values ('李四', 22, '销售部', 3000),('王五', 23, '技术部门', 20000);

insert into people values (6, '赵六', 1, 30, '财务部', 4000, 2);
insert into people set name='孙七', gender=1, age=33, department='销售部', salary=3000, is_married=2;
insert into people set name='周八', age=22, department='服务部', salary=3500;

insert into people(name, age, department, salary) values ('张三1', 38, '技术部门', 500.5), ('张三2', 38, '技术部门', 500.5) ;
insert into people(name, age, department, salary) values ('张三1', 18, '技术部门', 500.5), ('张三2', 33, '技术部门', 500.5) ;

# 删
# 删除数据
/*
    delete from + 表名 -->全部删除数据
    delete from + 表名 where 字段名=值 -->只删除where条件所筛选的行
        and -->与
        or -->或
        not -->非
*/
# delete from people ;
delete from people where name='张三1' and age=38 or name='张三2' and age=38 ;

# 改
# 修改数据 update + 表名 set + 字段名= + 新值 where 字段=/like 该字段值 # where表示条件筛选
update people set salary=salary+20000 where name='alex' ;
update people set salary=20000 where name='张三' ;
update people set gender=2 where name like '张三' ;


# 查
# 查询数据 select 字段名/(*) from 表名 [where条件语句]
select name from people;
select * from people ;
