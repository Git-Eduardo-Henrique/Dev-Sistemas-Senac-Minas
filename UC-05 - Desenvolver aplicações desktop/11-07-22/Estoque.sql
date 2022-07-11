# drop database estoque;
create database estoque;
use estoque;

create table Fabricantes (codigo int auto_increment primary key, nome varchar(70));

create table Produtos (id int auto_increment primary key, descricao varchar(70), quantidade int);

create table Saida (id int auto_increment primary key);

create table Compras (id int auto_increment primary key);

alter table Produtos 
add column codigo_fabri int, 
drop primary key,
add primary key (id, codigo_fabri),
add foreign key (codigo_fabri) references Fabricantes(codigo);

#Relacionamento N:N Compra
create table Compras_Produtos (cod_produtos int , id_compra int auto_increment, 
primary key (cod_produtos, id_compra), foreign key (cod_produtos) references Produtos(id),foreign key (id_compra) references Compras(id));

#Relacionamento N:N Saida
create table Saida_Produtos (cod_produtos int, id_saida int auto_increment, 
primary key (cod_produtos, id_saida), foreign key (cod_produtos) references Produtos(id),foreign key (id_saida) references Saida(id));

select * from Produtos;

select * from Fabricantes;
