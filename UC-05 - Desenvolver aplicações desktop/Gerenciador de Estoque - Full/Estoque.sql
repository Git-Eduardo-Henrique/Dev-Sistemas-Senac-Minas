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

# insert into Produtos (descricao, quantidade, valor, codigo_fabri) values ("mi 8 lite", 102030, 1000, 1);
# delete from Produtos where id > 0;
# =================================================  tabela Saida =======================================================================
create table saida (
id int auto_increment not null,
test varchar(10),
primary key(id));
# =================================================  tabela Compras ======================================================================
create table compra (
id int auto_increment not null,
test varchar(10),
primary key(id));
# =================================================  Relacionamento 1:1 ======================================================================
alter table Produtos 
add column codigo_fabri int, 
drop primary key,
add primary key (id, codigo_fabri),
add foreign key (codigo_fabri) references Fabricantes(codigo);
# =================================================  Relacionamento N:N Compra ======================================================================
create table compra_produtos (
cod_produtos int not null, 
id_compra int auto_increment,
data_compra datetime not null,
quantidade_compra int not null,
primary key (cod_produtos, id_compra), 
foreign key (cod_produtos) references Produtos(id),
foreign key (id_compra) references compra(id));
# =================================================  Relacionamento N:N Saida ======================================================================
create table saida_Produtos (
cod_produtos int not null, 
id_saida int auto_increment, 
data_saida datetime not null,
quantidade_saida int not null,
primary key (cod_produtos, id_saida), 
foreign key (cod_produtos) references Produtos(id),
foreign key (id_saida) references saida(id));
# ================================================================  SELECT'S =======================================================================
select * from Produtos;
select * from Fabricantes;
select * from compra_produtos;
select * from compra;
select * from saida;
select * from saida_Produtos;
select * from Funcionario;