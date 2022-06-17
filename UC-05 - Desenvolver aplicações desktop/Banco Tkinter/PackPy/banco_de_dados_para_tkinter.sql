create database Banco;
use Banco;

create table func(id_func varchar(30) primary key, cpf varchar(14));
select * from func;

create table cliente(cpf varchar(14) primary key, nome varchar(45), dataNasc datetime(6), genero enum("M","F"), email varchar(50), senha varchar(8));
select * from cliente;