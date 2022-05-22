create database empresa_mucho_loca;
use empresa_mucho_loca;

create table funcionarios(
CPF varchar(14),
nome varchar(45),
salario varchar(20),
telefone varchar(20),
endereço varchar(20),
primary key(CPF));

create table departamentos(
codigo int,
nome varchar(45),
localização varchar(100),
primary key(codigo));

create table depedentes(
codigo int,
nome varchar(45),
endereço varchar(45),
parentesco varchar(45),
primary key(codigo));

create table projetos(
numero int,
tipo varchar(45),
verba varchar(45),
nome varchar(45),
primary key(numero));

# projetos 1:1
# funcionarios 1:1
# funcionarios 1:n
# Projetos 1:n
alter table projetos add column CPF_funcionario varchar(14);
alter table funcionarios add column codigo_departamentoGerenciar int;
alter table funcionarios add column codigo_departamento int;
alter table projetos add column codigo_departamento int;

alter table projetos add foreign key(CPF_funcionario) references funcionarios(CPF);
alter table funcionarios add foreign key(codigo_departamentoGerenciar) references departamentos(codigo);
alter table funcionarios add foreign key(codigo_departamento) references departamentos(codigo);
alter table projetos add foreign key(codigo_departamento) references departamentos(codigo);

create table Funcionarios_Dependentes(
CPF_funcionario varchar(14), 
codigo_dependente int,
primary key(CPF_funcionario, codigo_dependente),
foreign key(CPF_funcionario) references funcionarios(CPF),
foreign key(codigo_dependente) references depedentes(codigo));

create table Funcionarios_Projetos(
CPF_funcionario varchar(14), 
numero_projeto int, 
numero_horas int,
primary key(CPF_funcionario, numero_projeto),
foreign key(CPF_funcionario) references funcionarios(CPF),
foreign key(numero_projeto) references projetos(numero));

insert into departamentos (codigo, nome, localização) 
values
(456, 'Tecnologia da Informação', 'quadra A-31'), 
(231, 'Financeiro', 'quadra A-25'), 
(556, 'Marketing', 'quadra A-12'),
(211, 'Jurídico', 'quadra A-13'), 
(120, 'Comercial', 'quadra B-01'), 
(466, 'Recursos Humanos', 'quadra C-14'), 
(560, 'Presidência', 'quadra C-11');

insert into funcionarios (CPF, nome, endereço, telefone, salario, codigo_departamento, codigo_departamentoGerenciar) 
values 
(10022256232, 'Olívia de Paula Brito', 'São Paulo', 314430089, 1200, 556, NULL),
(90856251432, 'Fernando Marciel', 'Santo André', 318907654, 2500, 456, NULL), 
(3985699025, 'Adilson Fernandes Souza', 'São Paulo', 314220065,4500,231,231),
(29845651111, 'Vanessa Brito', 'Sorocaba', 312678904, 950, 466, NULL),
(10546222142, 'Marcos Antonio da Silva', 'Jundiaí', 319786874, 980,456,NULL);

insert into depedentes (codigo, nome, endereço, parentesco) 
values
(3768, 'Leonardo Silva Marciel','','filho'), 
(3776, 'Mariana Lemos de Souza','','filha'), 
(2763, 'José Francisco Brito', '', 'pai'),
(3322, 'André Silva Marciel', '', 'filho'), 
(7316, 'Leandro Silva Marciel', '', 'filho');

insert into projetos (numero, nome, tipo, verba, codigo_departamento) 
values
(56, 'Alfa', 'integral-2 anos', 1500, 556), 
(12, 'D3RE', 'integral-1 anos', 1500, 211), 
(46, 'X3', 'parcial-2 anos', 5000, 456),
(47, 'Beta', 'parcial-2 anos', 1500, 556), 
(21, 'XR3', 'integral-5 anos', 2000, 456);

insert into Funcionarios_Dependentes (CPF_funcionario, codigo_dependente) 
values
(90856251432, 3322),
(90856251432, 7316),
(3985699025, 2763),
(29845651111, 2763),
(10546222142, 3776),
(10546222142, 3768);

insert into Funcionarios_Projetos (CPF_funcionario, numero_projeto, numero_horas) 
values
(90856251432, 12, 230), 
(90856251432, 56, 300),
(3985699025, 56, 120), 
(29845651111, 46, 248), 
(10546222142, 21, 30), 
(10546222142, 47, 20);

select * from Funcionarios_Projetos;
select * from depedentes;
set SQL_SAFE_UPDATES = 0;

# ATV 1
update depedentes set endereço = 'Pouso Alegre';
# ATV 2
select nome from funcionarios;
# ATV 3
select * from Funcionarios_Projetos order by numero_horas desc; 

