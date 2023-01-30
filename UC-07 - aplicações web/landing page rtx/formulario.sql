create database Formulario;
use Formulario;

create table formu(
	id int not null auto_increment,
    nome varchar(50) not null,
    email varchar(255) not null,
    whatsapp varchar(15) not null,
    primary key(id)
);

select * from formu;
#describe formu;
# drop database Formulario;