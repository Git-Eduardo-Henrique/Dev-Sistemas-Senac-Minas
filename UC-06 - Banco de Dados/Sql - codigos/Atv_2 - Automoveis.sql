create database Ze_do_pneu_automoveis;
use Ze_do_pneu_automoveis;

# 2.1
create table Cliente(
CPF varchar(11),
nome varchar(45),
numConta int,
telefone varchar(15),
cidade varchar(45),
primary key (CPF));

create table Carro(
CHASSI varchar(45),
modelo varchar(45),
cor varchar(45),
ano varchar(45),
valor float,
primary key (CHASSI));

create table Aluguel(
CHASSI varchar(45),
CPF varchar(11),
dataEntrada varchar(45),
dataSaida varchar(45),
total int,
primary key(CPF, CHASSI),
foreign key(CPF) references Cliente(CPF),
foreign key(CHASSI) references Carro(CHASSI));

#2.2
insert into Cliente(CPF, nome, numConta, telefone, cidade) values 
(111111, 'Ana', 2317, 019, 'Campinas'),
(222222, 'Fabio', 1711, 019, 'Jundiai'),
(121111, 'Maria', 7121, 011, 'SaoPaulo'),
(321222, 'Flavio', 2211, 019, 'Campinas'),
(123111, 'Fernando', 3211, 021, 'Belo Horizonte');

insert into Carro (CHASSI, modelo, cor, ano, valor) values
('A21','Uno','Prata','2003',null),
('2AC','Gol','Preto','2004',null),
('33A','Corsa','Branco','2005',null),
('12C','Uno','Verde','2001',null),
('1C2','Astra','Prata','2005',null),
('22A','Gol','Prata','2005',null);

insert into aluguel (CPF,CHASSI,dataEntrada,dataSaida,total) values
('111111','33a','21-07-2006','05-08-2006',null),
('222222','12c','21-07-2006',null,null),
('222222','33a','23-07-2006','06-08-2006',null),
('222222','1c2','24-07-2006',null,null);

#2.3
#a
insert into Cliente(CPF, nome, numConta, telefone, cidade) values 
('', null, null, null, null);

#b
insert into Carro(valor, cor, ano, CHASSI, modelo) values
('999999999999', 'laranja',  1210, '23L','Relanpago_Marquinhos');

#c
insert into Aluguel(CPF,CHASSI,dataEntrada,dataSaida,total) values
('111111', 'A21', '20-11-1662', '30-02-3092', 2),
('222222', '2AC', '30-10-1920', '20-09-2019', 1000),
('222222', '22A', '29-04-1505', '21-01-2001', 210000);

#d
SET SQL_SAFE_UPDATES = 0;
update Cliente set telefone = 019;

#e
update Cliente set nome = 'Andre' where CPF = '111111';

#f
update Cliente set cidade = 'Brasilia' where numConta > 2000;

#g
update Carro set valor = 20000;

#h
update Carro set cor = 'Azul' where modelo = 'Uno' or modelo = 'Corsa';

#i
update Aluguel set dataEntrada = 'nao sei' where CPF = '111111';

#j
update Aluguel set dataSaida = NULL;

#k
delete from Cliente where cidade = 'Campinas';

#l
delete from Aluguel where CHASSI = 'A21' OR CHASSI = '2AC';
delete from Carro where ano = '2003' OR ano = '2004';

#m
delete from aluguel where CHASSI = '22A';
delete from Carro where CHASSI = '22A';

#n
delete from Cliente where nome = 'Fernando';

#o
insert Carro values
('33B','Corsa','Branco','2005',null);
delete from aluguel where CHASSI = '33A' or CHASSI = '33B';
delete from Carro where CHASSI = '33A' or CHASSI = '33B';

#p
insert into Carro (CHASSI, modelo, cor, ano, valor) values
('3AC','Gol','Prata','2004',null);
insert into aluguel (CPF,CHASSI,dataEntrada,dataSaida,total) values
('222222', '3AC', '10-10-2010', '20-12-2011', 20102);
delete from aluguel where CHASSI = '3AC';
delete from Carro where CHASSI = '3AC';

#q
insert into Cliente (CPF, nome, numConta, telefone, cidade) values 
('234123', 'Cleitin', '410291', '19', 'Campinas');
delete from Cliente where telefone = '19' and cidade = 'Campinas';

#r
delete from Carro where valor < 2000 and valor > 1000;

#s
delete from aluguel where CPF <> 0 or CPF = null;

select * from Cliente; 
select * from aluguel;
select * from Carro;