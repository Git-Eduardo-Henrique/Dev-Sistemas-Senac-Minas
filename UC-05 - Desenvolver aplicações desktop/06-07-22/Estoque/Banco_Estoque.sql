create database estoque;
use estoque;

create table Fabricantes (codigo int auto_increment primary key, nome varchar(70));

create table Produtos (id int auto_increment primary key, descricao varchar(70), quantidade int);

alter table Produtos
add column codigo_fabri int, add foreign key (codigo_fabri) references Fabricantes(codigo);