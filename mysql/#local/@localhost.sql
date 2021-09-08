show processlist ;

select concat('drop table ', table_name,';') from information_schema.TABLES where TABLE_SCHEMA = 'eg_ajax' ;

use eg_ajax ;
show tables ;

select class.name, student.name, teacher.name
from ajax_student as student
         left join ajax_classes as class on student.class_id = class.id
         left join ajax_teachers as teacher
         left join ajax_classes_to_teachers as ct on ct.teachers_id = teacher.id on ct.classes_id = class.id
where student.name = '卢平';
