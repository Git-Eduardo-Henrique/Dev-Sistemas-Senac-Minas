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

select * from livros;
select * from funcionario;
select * from autores_livros;