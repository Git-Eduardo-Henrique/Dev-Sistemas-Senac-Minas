algoritmo "Firma dos cafeinado"
// Função :
// Autor : Eduardo Henrique
// Data : 30/11/2021
// Seção de Declarações 
var
Cadastro: vetor[0..5, 0..6] de caractere
salario: vetor[0..1,0..6] de real
contador: inteiro
inicio
// Seção de Comando
para contador de 0 ate 6 faca
  limpatela
  escreval("===============================================")
  escreval("============= Firma dos cafeinado =============")
  escreval("===============================================")
  escreval("Há iniciar cadastro do", contador + 1, "º funcionario...")
  escreval("===============================================")
  escreva("ID: ")
  leia(cadastro[0,0 + contador])
  escreval("===============================================")
  escreva("Nome: ")
  leia(cadastro[1,0 + contador])
  escreval("===============================================")
  escreva("Idade: ")
  leia(cadastro[2,0 + contador])
  escreval("===============================================")
  escreva("Sexo: ")
  leia(cadastro[3,0 + contador])
  escreval("===============================================")
  escreva("Cargo: ")
  leia(cadastro[4,0 + contador])
  escreval("===============================================")
  escreva("Salario: R$")
  leia(salario[0,0 + contador])
  escreval("===============================================")

  
fimpara
fimalgoritmo
