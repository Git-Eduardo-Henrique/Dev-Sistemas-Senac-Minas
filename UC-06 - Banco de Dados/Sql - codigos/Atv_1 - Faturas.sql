create database Faturas_oi;
use Faturas_oi;

#1.1
create table Cliente(
codCliente int,
nome varchar(45),
endereco varchar(45),
credito varchar(45),
tipo varchar(45),
CPF varchar(11),
primary key(codCliente));

create table fatura(
numFatura int,
codCliente_Cliente int,
primary key(numFatura),
foreign key(codCliente_Cliente) references Cliente(codCliente));

create table Produto(
codProduto int,
descricao varchar(45),
primary key(codProduto));

create table ItensFatura(
quantidade int,
valor float,
numFatura_fatura int,
codProduto_Produto int,
primary key(numFatura_fatura,codProduto_Produto),
foreign key(numFatura_fatura) references fatura(numFatura),
foreign key(codProduto_Produto) references Produto(codProduto));

# 1.2
alter table Cliente add column historico varchar(45) not null;
alter table Cliente modify column nome varchar(30);
alter table Cliente drop column credito;

# 1.3
rename table Fatura to Pedido;
alter table Pedido add column dataPed varchar(45);

# 1.4
alter table Produto add column precoCompra float;
alter table Produto modify column descricao varchar(25);

# 1.5
alter table ItensFatura add column precoVenda float;
alter table ItensFatura modify column quantidade int(5);
alter table ItensFatura drop column valor;
rename table ItensFatura to ItensPedido;
drop table ItensPedido;