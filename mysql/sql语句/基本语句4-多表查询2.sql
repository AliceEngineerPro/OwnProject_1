create table  tableA (
    id int primary key ,
    name varchar(20)

) ;

create table tableB(
    id int primary key ,
    name varchar(20) ,
    tableA_id int
) ;

insert into tableA values (1,'Alex'),
                          (2,'Jack'),
                          (3,'Amy') ;

insert into tableB values (1,'小雨',1),
                          (2,'彬彬',2),
                          (3,'洲洲',4) ;

# tableA
select * from tableA ;
# tableB
select * from tableB ;

# all
select * from tableA, tableB ;

select * from tableA, tableB where tableB.tableA_id=tableA.id ;

--
--

create table employee(
    id int primary key auto_increment comment '主键id',
    emp_name varchar(20) comment '名字',
    age int comment '年龄',
    dept_id int comment '部门ID'
) ;

insert into employee (emp_name, age, dept_id) values ('a', 19, 200),
                                                     ('b', 26, 201),
                                                     ('c', 30, 201),
                                                     ('d', 24, 200),
                                                     ('e', 20, 200),
                                                     ('f', 28, 204) ;

create table department(
    dept_id int comment '部门ID',
    dept_name varchar(20) comment '部门名字'
) ;

insert into department values (200, '人事部'),
                              (201, '技术部'),
                              (202, '销售部'),
                              (203, '财政部') ;

select * from employee ;
select * from department ;

select * from employee ,department ;

select employee.id, employee.emp_name, department.dept_name from department,employee where employee.dept_id=department.dept_id and employee.emp_name='a';

# 内连接查询 select * from 表1 inner join 表2 on [条件]
select employee.id ,employee.emp_name, department.dept_name from department inner join employee on employee.dept_id=department.dept_id and emp_name='a' ;

# 外连接查询
select employee.id, employee.emp_name, department.dept_name from employee left join department on employee.dept_id=department.dept_id ;
select employee.id, employee.emp_name, department.dept_name from department right join employee on employee.dept_id=department.dept_id ;
select employee.id, employee.emp_name, department.dept_name from department left join employee on employee.dept_id=department.dept_id ;
select employee.id ,employee.emp_name, department.dept_name from employee right join department on employee.dept_id=department.dept_id ;

select employee.emp_name from employee ,department where employee.dept_id = department.dept_id and department.dept_name = '技术部' ;

# 子查询 select * from + 表名 in (子语句)
