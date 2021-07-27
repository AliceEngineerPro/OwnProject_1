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


