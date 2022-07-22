# drop database estoque;
create database estoque;
use estoque;
# =================================================  tabela Funcionario =======================================================================
create table Funcionario (
nome varchar(70) not null,
codigo int not null,
primary key(codigo));

insert into Funcionario value ("Eduardo", 102030);
# =================================================  tabela Fabricante =======================================================================
create table Fabricantes (
codigo int auto_increment, 
nome varchar(70) not null,
cnpj varchar(18) not null,
primary key (codigo));
# =================================================  tabela Produtos =======================================================================
create table Produtos (
id int auto_increment not null, 
descricao varchar(70) not null, 
quantidade int not null, 
valor float not null,
primary key (id));
# =================================================  tabela Saida =======================================================================
create table Saida (
id int auto_increment not null,
primary key(id));
# =================================================  tabela Compras ======================================================================
create table Compras (
id int auto_increment not null,
primary key(id));
# =================================================  Relacionamento 1:1 ======================================================================
alter table Produtos 
add column codigo_fabri int, 
drop primary key,
add primary key (id, codigo_fabri),
add foreign key (codigo_fabri) references Fabricantes(codigo);
# =================================================  Relacionamento N:N Compra ======================================================================
create table Compras_Produtos (
cod_produtos int not null, 
id_compra int auto_increment not null, 
primary key (cod_produtos, id_compra), 
foreign key (cod_produtos) references Produtos(id),
foreign key (id_compra) references Compras(id));
# =================================================  Relacionamento N:N Saida ======================================================================
create table Saida_Produtos (
cod_produtos int not null, 
id_saida int auto_increment not null, 
primary key (cod_produtos, id_saida), 
foreign key (cod_produtos) references Produtos(id),
foreign key (id_saida) references Saida(id));
# ================================================================  SELECT'S =======================================================================
select * from Produtos;
select * from Fabricantes;
select * from Compras_Produtos;
select * from Saida_Produtos;
select * from Funcionario;