create database crud;
use crud;

create table pessoas(
id int auto_increment,
nome varchar(45),
dataNasc date,
primary key (id));

select * from pessoas;
insert into pessoas value(1, 'Rodrigo', '2022-07-05')