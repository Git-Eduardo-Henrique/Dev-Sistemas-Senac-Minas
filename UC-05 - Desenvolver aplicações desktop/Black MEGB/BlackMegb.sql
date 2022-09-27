create database blackmegb;
use blackmegb;

create table Usuarios(
id int auto_increment primary key,
nome varchar(25),
sobrenome varchar(25),
nome_exibicao varchar(45),
email varchar(60),
senha varchar(8),
total_jogos int);

create table jogos (
id int auto_increment primary key,
nome varchar(45));

insert into jogos (nome) values 
('Super Mario World'),('Sonic'), ('Donkey Kong'), ('Mortal Kombat 3'), ('Super Bomberman');

select * from jogos;
select * from Usuarios;

# drop database blackmegb;