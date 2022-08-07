create database blackmegb;
use blackmegb;

create table Usuarios(
id int auto_increment primary key,
nome varchar(25),
sobrenome varchar(25),
nome_exibicao varchar(45),
email varchar(60),
senha varchar(8));

select * from Usuarios;