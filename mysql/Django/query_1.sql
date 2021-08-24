create database django_temp character set 'utf8';
use django_temp ;
show tables ;
desc app01_publish ;
show full columns from app01_publish ;

select * from app01_publish ;
select * from app01_book ;
select * from app01_author ;
select * from app01_bookandauthor;

update app01_publish set city = '北京' where name = '机械出版社' ;

show full processlist ;

select * from app01_book where id in (3, 5, 1) ;

create database django_temp_demo1 charset 'utf8';

show create database django_temp1_demo1 ;
