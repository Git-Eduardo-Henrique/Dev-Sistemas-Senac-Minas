create database livraria_mucho_top;
use livraria_mucho_top;

create table usuarios (
cpf varchar(14) ,
nome varchar(45) ,
telefone varchar(45) ,
endereco varchar(45),
primary key (cpf));

create table funcionario (
cpf varchar(14) ,
nome varchar(45) ,
telefone varchar(45) ,
endereco varchar(45),
salario float,
funcao varchar(45) ,
primary key (cpf));

create table livros (
id_livros varchar(45) ,
genero varchar(45) ,
titulo varchar(114) ,
edicao varchar(45) ,
ano_pub varchar(45) ,
primary key (id_livros));

create table autores(
nome varchar(45),
id_autores varchar(45) ,
nacionalidade varchar(45),
primary key (id_autores));

create table editoras (
id_editoras varchar(45) ,
nome varchar(45),
contato varchar(30),
endereco varchar(45),
primary key(id_editoras));

# funcionarios para livros 1:n
# editoras para livros 1:n
# usuarios para livros 1:n
# usuarios para livros 1:1
alter table livros add column id_edi varchar(45);
alter table livros add column cpf_fun varchar(14) ;
alter table livros add column cpf_usu varchar(14) ;
alter table livros add column cpf_usu_uni varchar(14)  unique;
alter table livros drop primary key;
alter table livros add primary key(id_livros,id_edi);
alter table livros add foreign key(cpf_fun) references funcionario(cpf);
alter table livros add foreign key(id_edi) references editoras(id_editoras);
alter table livros add foreign key(cpf_usu) references usuarios(cpf);
alter table livros add foreign key(cpf_usu_uni) references usuarios(cpf);

create table autores_livros (
id_livros_livros varchar(45) ,
id_autores_autores varchar(45) ,
primary key(id_livros_livros,id_autores_autores),
foreign key(id_livros_livros) references livros(id_livros),
foreign key(id_autores_autores) references autores(id_autores));

insert into funcionario (cpf, nome, endereco, telefone, salario, funcao) values
(30361290876, 'Ademir José Silva', 'Campinas', 22317865, 0, NULL),
(23161197770, 'Ana Salles Azir', 'Salto', 22317865,0, 'Recepcionista'),
(61254590871, 'Lucia Vicentim', 'Salto', 21316565, 0, 'Bibliotecaria'), 
(20321295096, 'João Alberto Smith', 'Itatiba', 22447865, 0, NULL), 
(32361298734, 'Luís Henrique Talles', 'Campinas', 21531785, 0, NULL), 
(45403612087, 'Francisco José Almeida', 'Indaiatuba', 25417761, 0, NULL);

insert into editoras values 
(2134000, 'Saraiva', 'São Paulo', 08003434), 
(2287000, 'Eras', 'Brasília', 08002432), 
(3557000, 'Summer', 'Curitiba', 08002198), 
(6655000, 'Pontos', 'São Paulo', 08005600), 
(9898000, 'Marks', 'Rio de Janeiro', 08009000);

insert into usuarios (cpf, nome, telefone, endereco) 
values
(10122020232, 'Maria de Lourdes Amaral', 35440089, NULL), 
(19321122213, 'José Francisco de Paula', 27219756, NULL), 
(70964411900, 'Luiza Souza Prado', 34559087, NULL), 
(45399109881, 'Raquel Santos', 87603451, NULL), 
(22539910976, 'Ivete Medina Chernell', 48170352, NULL);

insert into autores (nome, nacionalidade,id_autores) 
values
('Ethevaldo Siqueira', 'Brasileira',85668900), 
('Ana Lucia Jankovic Barduchi', 'Brasileira',77548854), 
('Adélia Prado', 'Brasileira',55490076),
('Walter Isaacson', 'Americana',22564411), 
('Steven K. Scott', 'Americana',90984133);

insert into livros (id_livros, titulo, genero, edicao, ano_pub, cpf_fun, id_edi, cpf_usu, cpf_usu_uni) 
values
(87659908, 'Tecnologias que Mudam Nossa Vida', 'Tecnologia', 2, 2007, NULL, 2134000, NULL, 70964411900),
(67392217, 'Empregabilidade – Competências Pessoais e Profissionais', 'Administração', 22, 1977, 32361298734, 9898000,NULL, NULL), 
(45112239, 'Steve Jobs – a Biografia', 'Biografia', 48, 2011, NULL, 2287000, 19321122213, NULL),
(77680012, 'A Duração do Dia', 'Poesia', 1, 2010,NULL,2134000, 10122020232, NULL), 
(32176500, 'Salomão – O Homem Mais Rico que Já Existiu', 'Romance', 2,2011, 61254590871, 6655000, NULL, NULL),
(67554421, 'Bagagem', 'Poesia', 5,1972,NULL, 6655000, NULL, NULL), 
(10277843, 'O Pelicano', 'Romance', 12, 1984,NULL, 2134000, NULL, NULL);

insert into autores_livros (id_livros_livros, id_autores_autores) 
values
(10277843,55490076),
(32176500,90984133),
(45112239,22564411),
(67392217,77548854),
(67554421,55490076),
(77680012,55490076),
(87659908,85668900),
(10277843,85668900),
(32176500,22564411);

# atv 1 
update funcionario set salario = '800' where cpf = '32361298734';
update funcionario set funcao = 'auxiliar de biblioteca' where cpf = '32361298734';
select * from funcionario;
# atv 2
delete from usuarios where cpf = '45399109881';
# atv 3
delete from autores_livros where id_autores_autores = '90984133';
# atv 4
update livros set cpf_usu = '70964411900' where id_livros = '87659908';
update livros set cpf_usu_uni = NULL where id_livros = '87659908';
# atv 5
update livros set cpf_usu_uni = '70964411900' where id_livros = '10277843';

select * from usuarios;
select * from funcionario;
select * from Livros;
select * from autores_livros;
select * from autores;