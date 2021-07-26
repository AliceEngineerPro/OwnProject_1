use learn_db ;

# 创建主表
create table class_teachers(
    id int primary key auto_increment not null comment '班主任ID',
    name varchar(20) not null comment '班主任名字' ,
    gender boolean default 0 comment '0:保密,1:男,2:女' ,
    age int comment '班主任年龄'

) ;
# 主表插入数据
insert into class_teachers(name, gender, age) values ('冰冰', 2, 22),
                                                     ('丹丹', 2, 25),
                                                     ('歪歪', 1, 27),
                                                     ('珊珊', 2, 26),
                                                     ('小雨', 2, 30);

# 创建子表
create table class_students(
    id int primary key auto_increment not null comment '学生ID',
    name varchar(20) not null comment '学生姓名' ,
    teacher_id int not null comment '班主任ID'

) engine = innodb ;

# 子表插入数据
insert into class_students(name, teacher_id) values ('学生1', 2),
                                                    ('学生2', 4),
                                                    ('学生3', 1),
                                                    ('学生4', 3),
                                                    ('学生5', 1),
                                                    ('学生6', 3),
                                                    ('学生7', 2) ;

# 查询主表
select * from class_teachers ;
# 查询子表
select * from class_students ;

# 创建外键
drop table class_students;
show tables ;

create table class_students(
    id int primary key auto_increment not null comment '学生ID',
    name varchar(20) not null comment '学生姓名' ,
    teacher_id int not null comment '班主任ID' ,
    foreign key (teacher_id) references class_teachers(id)

) engine = innodb ;

insert into class_students(name, teacher_id) values ('学生1', 2),
                                                    ('学生2', 4),
                                                    ('学生3', 5),
                                                    ('学生4', 3),
                                                    ('学生5', 5),
                                                    ('学生6', 3),
                                                    ('学生7', 2) ;

# teacher
select * from class_teachers ;
# student
select * from class_students ;


# 插如外键
show create table class_students2 ;
alter table class_students2 add constraint teacher_id foreign key (teacher_id) references class_teachers(id) ;
show create table class_students2 ;
# 删除外键
alter table class_students2 drop foreign key teacher_id ;
show create table class_students2 ;

select * from class_students, class_teachers ;
select * from class_teachers, class_students ;

select * from class_teachers, class_students where class_teachers.id=class_students.teacher_id ;
select * from class_students,class_teachers where class_students.teacher_id=class_teachers.id ;
select class_students.name, class_teachers.name from class_students,class_teachers where class_students.teacher_id=class_teachers.id ;
