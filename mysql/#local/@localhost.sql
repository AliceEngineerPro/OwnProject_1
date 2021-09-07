show processlist ;

select concat('drop table ', table_name,';') from information_schema.TABLES where TABLE_SCHEMA = 'eg_ajax' ;

use eg_ajax ;
show tables ;

